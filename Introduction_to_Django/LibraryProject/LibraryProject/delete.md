book.delete()

books = Book.objects.all()
if not books.exists():
    print("Book deleted successfully!")
else:
    print("Deletion failed!")