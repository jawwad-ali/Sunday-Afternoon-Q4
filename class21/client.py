import asyncio
from fastmcp import Client
import rich

client = Client("http://127.0.0.1:8000/sse")

async def main():
    async with client:
        # Read all books
        all_books = await client.read_resource("data://books")
        rich.print("All Books:", all_books)

        # Read a single book by id
        book = await client.read_resource("data://books/1")
        rich.print("Book 1:", book)

        # Read rules
        rules = await client.read_resource("data://rules")
        rich.print("Rules:", rules)

        rich.print("========================================== Tools: ========================================== ")

        # Issue a book
        issue_result = await client.call_tool("issue_book", {"book_id": 1})
        rich.print("Issue Book 1:", issue_result)

        # Try issuing the same book again (should fail)
        issue_again = await client.call_tool("issue_book", {"book_id": 1})
        rich.print("Issue Book 1 again:", issue_again)

        # Return the book
        return_result = await client.call_tool("return_book", {"book_id": 1})
        rich.print("Return Book 1:", return_result)

        rich.print("========================================== Prompts: ========================================== ")

        # Book recommendation prompt
        recommendation = await client.get_prompt("book_recommendation", {"genre": "Programming"})
        rich.print("Book Recommendation:", recommendation)

        # Overdue notice prompt
        overdue = await client.get_prompt("overdue_notice", {"user_name": "Ali", "book_id": 3})
        rich.print("Overdue Notice:", overdue)

if __name__ == "__main__":
    asyncio.run(main())
