// Create a LibraryCatalog class that handles the cataloging and management of
// books in a library. Implement methods to add new books, search for books by
// title or author, keep track of available copies, and display book details.
// class Book{
//   constructor(title,author,copies){
//     this.title = title; 
//     this.author = author; 
//     this.copies = copies;
//   }

// }
// class LibraryCatalog extends Book{
//   constructor(){
//     this.books = [];
//   }

//   addBook(){
//     const newBook = new Book(this.title, this.author, this.copies);
//     this.books.push(newBook);
//   }

//   searchByTitle(title){
//     const availableBooks = [];
//     for (let i = 0; i < availableBooks.length; i++) {
//       if (this.books[i].title === title) {
//         this.books[i].copies += num;        
//       }
      
//     }
//     return availableBooks;
//   }

//   updateCopies(title, num){
//     // const availableCopies = [];
//     for (let i = 0 ; i < this.books.length; i++){
//       if(this.books[i].title===title){
//         this.books[i].copies +=num;
//       }
//     }
//   }

//   getAvailableCopies(title) {
//     for (let i = 0; i < this.books.length; i++) {
//       if (this.books[i].title === title) {
//         return this.books[i].copies;
//       }
//     }
//     return 0;
//   }
// }

// const catalog = new LibraryCatalog();
// catalog.addBook("River", "Source", 1);
// catalog.updateCopies("River", 5);
// const availableCopies = catalog.getAvailableCopies("River");
// console.log(`Available copies of 'River': ${availableCopies}`);

// const searchedBooks = catalog.search("River");
// for (let i = 0; i < searchedBooks.length; i++) {
//   console.log(searchedBooks[i]);
// }


class Book {
  constructor(title, author, copies) {
    this.title = title;
    this.author = author;
    this.copies = copies;
  }
}

class LibraryCatalog {
  constructor() {
    this.books = [];
  }

  addBook(title, author, copies) {
    const newBook = new Book(title, author, copies);
    this.books.push(newBook);
  }

  searchByTitle(title) {
    const availableBooks = [];
    for (let i = 0; i < this.books.length; i++) {
      if (this.books[i].title === title) {
        availableBooks.push(this.books[i]);
      }
    }
    return availableBooks;
  }

  updateCopies(title, num) {
    for (let i = 0; i < this.books.length; i++) {
      if (this.books[i].title === title) {
        this.books[i].copies += num;
      }
    }
  }

  getAvailableCopies(title) {
    for (let i = 0; i < this.books.length; i++) {
      if (this.books[i].title === title) {
        return this.books[i].copies;
      }
    }
    return 0;
  }
}

const catalog = new LibraryCatalog();
catalog.addBook("River", "Source", 1);
catalog.updateCopies("River", 5);
const availableCopies = catalog.getAvailableCopies("River");
console.log(`Available copies of 'River': ${availableCopies}`);

const searchedBooks = catalog.searchByTitle("River");
for (let i = 0; i < searchedBooks.length; i++) {
  console.log(searchedBooks[i]);
}

  
 



// class Product {
//     constructor(name, price, quantity) {
//       this.name = name;
//       this.price = price;
//       this.quantity = quantity;
//     }
  
//     calculateTotalValue() {
//       return this.price * this.quantity;
//     }
//   }
  
//   // Create multiple objects of the Product class
//   const product1 = new Product("Apple", 1.0, 10);
//   const product2 = new Product("Banana", 0.5, 20);
//   const product3 = new Product("Orange", 0.75, 15);
  
//   // Calculate the total values
// //   const totalValue1 = product1.calculateTotalValue();
//   const totalValue2 = product2.calculateTotalValue();
//   const totalValue3 = product3.calculateTotalValue();
  
//   // Print the total values
//   console.log(`Total value of ${product1.name}: ${product1.calculateTotalValue()}`);
//   console.log(`Total value of ${product2.name}: ${totalValue2}`);
//   console.log(`Total value of ${product3.name}: ${totalValue3}`);
  