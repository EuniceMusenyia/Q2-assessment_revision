class Product {
    constructor(name, price, quantity) {
      this.name = name;
      this.price = price;
      this.quantity = quantity;
    }
  
    calculateTotalValue() {
      return this.price * this.quantity;
    }
  }
  
  // Create multiple objects of the Product class
  const product1 = new Product("Apple", 1.0, 10);
  const product2 = new Product("Banana", 0.5, 20);
  const product3 = new Product("Orange", 0.75, 15);
  
  // Calculate the total values
//   const totalValue1 = product1.calculateTotalValue();
  const totalValue2 = product2.calculateTotalValue();
  const totalValue3 = product3.calculateTotalValue();
  
  // Print the total values
  console.log(`Total value of ${product1.name}: ${product1.calculateTotalValue()}`);
  console.log(`Total value of ${product2.name}: ${totalValue2}`);
  console.log(`Total value of ${product3.name}: ${totalValue3}`);
  