from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output the created book
print(book)


# Retrieve the book
book = Book.objects.get(id=1)

# Display the book's details
print(book)


# Update the book's title
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated book
print(book)

# Delete the book
book.delete()

# Try to retrieve the book again
try:
    book = Book.objects.get(id=1)
except Book.DoesNotExist:
    print("The book has been deleted.")

## Create Operation

**Python Command:**
```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output the created book
print(book)


#### `retrieve.md`

```markdown
## Retrieve Operation

**Python Command:**
```python
# Retrieve the book
book = Book.objects.get(id=1)

# Display the book's details
print(book)


#### `update.md`

```markdown
## Update Operation

**Python Command:**
```python
# Update the book's title
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated book
print(book)


#### `delete.md`

```markdown
## Delete Operation

**Python Command:**
```python
# Delete the book
book.delete()

# Try to retrieve the book again
try:
    book = Book.objects.get(id=1)
except Book.DoesNotExist:
    print("The book has been deleted.")


