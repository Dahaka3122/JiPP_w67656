open System

type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages
    member this.GetInfo() = sprintf "Tytuł: %s, Autor: %s, Strony: %d" this.Title this.Author this.Pages

type User(name: string) =
    let mutable borrowedBooks: Book list = []
    member this.Name = name
    member this.BorrowBook(book: Book, library: Library) =
        if library.RemoveBook(book) then
            borrowedBooks <- book :: borrowedBooks
            printfn "Użytkownik %s wypożyczył książkę: %s" this.Name book.Title
        else
            printfn "Książka %s jest niedostępna w bibliotece." book.Title
    member this.ReturnBook(book: Book, library: Library) =
        if List.contains book borrowedBooks then
            borrowedBooks <- List.filter ((<>) book) borrowedBooks
            library.AddBook(book)
            printfn "Użytkownik %s zwrócił książkę: %s" this.Name book.Title
        else
            printfn "Książka %s nie była wypożyczona przez użytkownika %s." book.Title this.Name

and Library() =
    let mutable books: Book list = []
    member this.AddBook(book: Book) =
        books <- book :: books
        printfn "Dodano książkę: %s" book.Title
    member this.RemoveBook(book: Book) =
        if List.contains book books then
            books <- List.filter ((<>) book) books
            true
        else
            false
    member this.ListBooks() =
        if books.Length > 0 then
            books |> List.iter (fun book -> printfn "%s" (book.GetInfo()))
        else
            printfn "Biblioteka jest pusta."

[<EntryPoint>]
let main argv =
    let library = Library()

    let book1 = Book("Wiedźmin", "Andrzej Sapkowski", 320)
    let book2 = Book("Hobbit", "J.R.R. Tolkien", 310)
    let book3 = Book("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 328)

    library.AddBook(book1)
    library.AddBook(book2)
    library.AddBook(book3)

    printfn "\nKsiążki w bibliotece:"
    library.ListBooks()

    let user = User("Jan Kowalski")

    user.BorrowBook(book1, library)
    user.BorrowBook(book2, library)

    printfn "\nKsiążki w bibliotece po wypożyczeniu:"
    library.ListBooks()

    user.ReturnBook(book1, library)

    printfn "\nKsiążki w bibliotece po zwrocie:"
    library.ListBooks()

    0
