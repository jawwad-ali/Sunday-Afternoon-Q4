"""
Custom function tools for the Gemini Agent.
These tools extend the agent's capabilities with unique functionality.
"""

import re
from typing import Dict, List
from agents import function_tool
import urllib.request
from html.parser import HTMLParser
from duckduckgo_search import DDGS


class MetadataParser(HTMLParser):
    """HTML parser to extract metadata from web pages"""

    def __init__(self):
        super().__init__()
        self.metadata = {
            "title": None,
            "description": None,
            "og_title": None,
            "og_description": None,
            "og_image": None,
        }

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "title":
            self.in_title = True

        elif tag == "meta":
            # Standard meta description
            if attrs_dict.get("name") == "description":
                self.metadata["description"] = attrs_dict.get("content")

            # Open Graph metadata
            property_value = attrs_dict.get("property", "")
            if property_value == "og:title":
                self.metadata["og_title"] = attrs_dict.get("content")
            elif property_value == "og:description":
                self.metadata["og_description"] = attrs_dict.get("content")
            elif property_value == "og:image":
                self.metadata["og_image"] = attrs_dict.get("content")

    def handle_data(self, data):
        if hasattr(self, 'in_title') and self.in_title:
            self.metadata["title"] = data.strip()
            self.in_title = False


@function_tool
def fetch_url_metadata(url: str) -> Dict[str, str]:
    """
    Fetches and extracts metadata from a given URL including title, description,
    and Open Graph data. Useful for analyzing web pages and getting summaries.

    Args:
        url: The complete URL to fetch metadata from (must include http:// or https://)

    Returns:
        A dictionary containing the page's title, description, Open Graph title,
        Open Graph description, and Open Graph image URL if available.
    """
    try:
        # Validate URL format
        if not url.startswith(("http://", "https://")):
            return {"error": "URL must start with http:// or https://"}

        # Fetch the web page
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MetadataBot/1.0)"}
        request = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(request, timeout=10) as response:
            html_content = response.read().decode("utf-8", errors="ignore")

        # Parse HTML to extract metadata
        parser = MetadataParser()
        parser.feed(html_content)

        # Build result
        result = {
            "url": url,
            "title": parser.metadata["title"] or "No title found",
            "description": parser.metadata["description"] or "No description found",
            "og_title": parser.metadata["og_title"] or "Not available",
            "og_description": parser.metadata["og_description"] or "Not available",
            "og_image": parser.metadata["og_image"] or "Not available",
        }

        return result

    except urllib.error.URLError as e:
        return {"error": f"Failed to fetch URL: {str(e)}"}
    except Exception as e:
        return {"error": f"Error parsing metadata: {str(e)}"}


@function_tool
def analyze_text(text: str) -> Dict[str, any]:
    """
    Analyzes text and provides detailed statistics including word count, character count,
    sentence count, average word length, reading time, and identifies the longest word.
    Useful for content analysis and readability assessment.

    Args:
        text: The text content to analyze

    Returns:
        A dictionary containing:
        - word_count: Total number of words
        - character_count: Total characters (including spaces)
        - character_count_no_spaces: Characters excluding spaces
        - sentence_count: Number of sentences
        - paragraph_count: Number of paragraphs
        - average_word_length: Average length of words in characters
        - reading_time_minutes: Estimated reading time (assuming 200 words per minute)
        - longest_word: The longest word in the text
        - unique_words: Number of unique words (case-insensitive)
    """
    try:
        if not text or not text.strip():
            return {"error": "Text cannot be empty"}

        # Basic counts
        character_count = len(text)
        character_count_no_spaces = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))

        # Word analysis
        words = re.findall(r'\b\w+\b', text.lower())
        word_count = len(words)
        unique_words = len(set(words))

        # Calculate average word length
        if word_count > 0:
            total_word_length = sum(len(word) for word in words)
            average_word_length = round(total_word_length / word_count, 2)
            longest_word = max(words, key=len)
        else:
            average_word_length = 0
            longest_word = "N/A"

        # Sentence count (split by . ! ?)
        sentences = re.split(r'[.!?]+', text)
        sentence_count = len([s for s in sentences if s.strip()])

        # Paragraph count (split by double newlines or single newlines)
        paragraphs = [p for p in text.split('\n') if p.strip()]
        paragraph_count = len(paragraphs)

        # Reading time (average reading speed: 200 words per minute)
        reading_time_minutes = round(word_count / 200, 2) if word_count > 0 else 0

        return {
            "word_count": word_count,
            "character_count": character_count,
            "character_count_no_spaces": character_count_no_spaces,
            "sentence_count": sentence_count,
            "paragraph_count": paragraph_count,
            "average_word_length": average_word_length,
            "reading_time_minutes": reading_time_minutes,
            "longest_word": longest_word,
            "unique_words": unique_words,
            "lexical_diversity": round(unique_words / word_count, 2) if word_count > 0 else 0
        }

    except Exception as e:
        return {"error": f"Error analyzing text: {str(e)}"}


@function_tool
def web_search(query: str, max_results: int = 5) -> List[Dict[str, str]]:
    """
    Performs a web search using DuckDuckGo and returns relevant results.
    Useful for finding current information, news, articles, and answering questions
    that require up-to-date knowledge from the internet.

    Args:
        query: The search query string to look up on the web
        max_results: Maximum number of search results to return (default: 5, max: 10)

    Returns:
        A list of search results, where each result contains:
        - title: The title of the search result
        - href: The URL of the result
        - body: A snippet/description of the content
    """
    try:
        if not query or not query.strip():
            return [{"error": "Search query cannot be empty"}]

        # Limit max_results to reasonable range
        max_results = min(max(1, max_results), 10)

        # Perform search using DuckDuckGo
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))

        # Format results
        formatted_results = []
        for result in results:
            formatted_results.append({
                "title": result.get("title", "No title"),
                "href": result.get("href", ""),
                "body": result.get("body", "No description available"),
            })

        if not formatted_results:
            return [{"message": "No results found for the query"}]

        return formatted_results

    except Exception as e:
        return [{"error": f"Error performing web search: {str(e)}"}]
