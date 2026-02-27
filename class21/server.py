import json
from fastmcp import FastMCP

mcp = FastMCP()

with open("data/books.json") as f:
    books_data = json.load(f)

with open("data/rules.json") as r:
    rules = json.load(r)

######
################## Resources ##################
######

@mcp.resource("data://books")
async def get_all_books():
    return json.dumps(books_data)

@mcp.resource("data://books/{id}")
async def get_book_by_id(id: int):
    for book in books_data["books"]:
        if book["id"] == id:
            return json.dumps(book)
    return json.dumps({"error": f"Book with id {id} not found"})

@mcp.resource("data://rules")
async def get_rules():
    return json.dumps(rules)

######
################## Tools ##################
######

@mcp.tool()
async def issue_book(book_id: int) -> str:
    for book in books_data["books"]:
        if book["id"] == book_id:
            if not book["available"]:
                return json.dumps({"error": f"'{book['title']}' is already issued"})
            book["available"] = False
            return json.dumps({"success": f"'{book['title']}' has been issued"})
    return json.dumps({"error": f"Book with id {book_id} not found"})

@mcp.tool()
async def return_book(book_id: int) -> str:
    for book in books_data["books"]:
        if book["id"] == book_id:
            if book["available"]:
                return json.dumps({"error": f"'{book['title']}' is not issued"})
            book["available"] = True
            return json.dumps({"success": f"'{book['title']}' has been returned"})
    return json.dumps({"error": f"Book with id {book_id} not found"})

######
################## Prompts ##################
######

@mcp.prompt()
def book_recommendation(genre: str) -> str:
    available_books = [book for book in books_data["books"] if book["available"] and book["genre"].lower() == genre.lower()]
    if not available_books:
        return f"No available books found in the '{genre}' genre. Suggest some popular {genre} books the library should add."
    book_list = "\n".join([f"- {b['title']} by {b['author']} ({b['published_year']})" for b in available_books])
    return f"Here are available books in the '{genre}' genre:\n{book_list}\nRecommend which one the user should read and why."

@mcp.prompt()
def overdue_notice(user_name: str, book_id: int) -> str:
    for book in books_data["books"]:
        if book["id"] == book_id:
            return f"Write a polite overdue notice for {user_name} who has not returned '{book['title']}' by {book['author']}. Remind them of library rules and ask them to return it soon."
    return f"Write a general overdue notice for {user_name} reminding them to return their overdue library book."

if __name__ == "__main__":
    mcp.run()
