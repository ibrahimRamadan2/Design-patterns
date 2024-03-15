# Advanced Dynamic Tax Calculation System

## Project Overview

Develop an advanced system that dynamically calculates taxes for invoices with multiple items, supporting different tax calculation strategies. These strategies depend on various factors such as the country, product type, and customer status. This project challenges you to apply the Strategy Pattern to accommodate these variations efficiently and flexibly.

## Scenario

Your system needs to handle tax calculations with specific rules based on:
- **Country**
- **Product Type**
- **Customer Status**

The goal is to create a system where new tax rules can be added or existing ones changed with minimal impact on the overall system design.

## Specific Task: Calculate Tax for a Luxury Item in the US for a Premium Customer

### Requirements:

- **Country**: US
- **Product Type**: Luxury Item
- **Customer Status**: Premium

### Tax Rules

- The standard tax rate in the US is **7%**.
- Luxury items have an additional **luxury tax of 5%**.
- Premium customers enjoy a **1% discount** on the total tax rate.

### Implementation Details

1. **Define Tax Calculation Strategies**: Implement strategies for tax calculation considering country, product type, and customer status. Specifically, account for US tax rules for luxury items and premium customer status.
2. **Strategy Selection Mechanism**: Design the system to dynamically choose the correct tax strategy based on the invoice details.
3. **Apply the Strategy Pattern**: Use the Strategy Pattern to encapsulate each tax calculation algorithm, ensuring the system's flexibility and extensibility.

### Challenges

- **Extensibility**: The system should easily accommodate new tax rules or changes in the existing ones.
- **Combining Strategies**: Some scenarios may require combining multiple tax strategies to compute the correct tax.
- **Optimization**: Ensure the system remains performant, especially when processing invoices with numerous items.

## Expected Outcome

A flexible and efficient tax calculation system that correctly applies US tax rules for a luxury item purchased by a premium customer, demonstrating the practical use of the Strategy Pattern in managing complex conditional logic and enhancing system maintainability.

### Note: this app can expand and support all countries tax calculations, with this pattern for Example add Germany tax calculator.

### class diagram
![image](https://github.com/ibrahimRamadan2/Design-patterns/assets/110139860/a3487129-2e14-4c04-8703-18c889024cf3)

