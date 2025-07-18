# Coffee Machine Program Requirements

---

### 1. Prompt user by asking:
**“What would you like? (espresso/latte/cappuccino):”**

- Check the user’s input to decide what to do next.
- The prompt should show every time an action has completed (e.g., once the drink is dispensed).
- The prompt should show again to serve the next customer.

---

### 2. Turn off the Coffee Machine by entering:
**“off”**

- For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
- Your code should end execution when this happens.

---

### 3. Print report

- When the user enters “report” to the prompt, a report should be generated that shows the current resource values.

Example:
```
Water: 100ml  
Milk: 50ml  
Coffee: 76g  
Money: $2.5
```

---

### 4. Check resources sufficient?

- When the user chooses a drink, the program should check if there are enough resources to make that drink.
- If Latte requires 200ml water but there is only 100ml left in the machine, it should not continue to make the drink but print:
  > “Sorry there is not enough water.”
- The same should happen if another resource is depleted (e.g., milk or coffee).

---

### 5. Process coins

- If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
- Coin values:
  - Quarters = $0.25
  - Dimes = $0.10
  - Nickels = $0.05
  - Pennies = $0.01
- Calculate the monetary value of the coins inserted.

Example:
```
1 quarter, 2 dimes, 1 nickel, 2 pennies  
= 0.25 + 0.10×2 + 0.05 + 0.01×2 = $0.52
```

---

### 6. Check transaction successful?

- Check that the user has inserted enough money to purchase the drink they selected.

Example:
- Latte costs $2.50, but they only inserted $0.52 →  
  > “Sorry that's not enough money. Money refunded.”

- If the user has inserted enough money:
  - The cost of the drink gets added to the machine as profit.
  - This will be reflected the next time “report” is triggered.

Example:
```
Water: 100ml  
Milk: 50ml  
Coffee: 76g  
Money: $2.5
```

- If the user has inserted too much money, the machine should offer change.

Example:
> “Here is $2.45 dollars in change.”  
(Change should be rounded to 2 decimal places.)

---

### 7. Make Coffee

- If the transaction is successful and there are enough resources:
  - Deduct the ingredients from the coffee machine resources.

Example:
**Before purchasing latte:**
```
Water: 300ml  
Milk: 200ml  
Coffee: 100g  
Money: $0
```

**After purchasing latte:**
```
Water: 100ml  
Milk: 50ml  
Coffee: 76g  
Money: $2.5
```

- Once all resources have been deducted, tell the user:
  > “Here is your latte. Enjoy!”

---
