class Category:
  category: str
  balance: float
  ledger: list

  def __init__(self, category):
    try:
      self.category = category
    except Exception as err:
      print(err)
    self.balance = 0.0
    self.ledger = []
  
  def __str__(self):
    print_width = 30
    res = self.category.center(print_width, "*") + "\n"
    for entry in self.ledger:
      print(entry["description"])
      res += f"{entry['description']:<23.23}{entry['amount']:>7.2f}\n"
    res += f"Total: {self.balance:<.2f}".format("<30.30")
    return res
  
  def deposit(self, amount, description=""):
    try:
      self.ledger.append({"amount": amount, "description": description})
      self.balance += amount
    except Exception as err:
      print(err)

  def withdraw(self, amount, description=""):
    try:
      if self.check_funds(amount):
        self.ledger.append({"amount": -amount, "description": description})
        self.balance -= amount
        return True
      else:
        return False        
    except Exception as err:
      print(err)

  def get_total_withdrawals(self):
    withdrawals_list = (entry["amount"] for entry in self.ledger if entry["amount"] < 0)
    res = 0.0
    for i in withdrawals_list:
      res += i
    return res
    
  def get_balance(self):
    return self.balance
  
  def transfer(self, amount, transfer_category):
    try:
      if self.check_funds(amount):
        self.withdraw(amount, f"Transfer to {transfer_category.category}")
        transfer_category.deposit(amount, f"Transfer from {self.category}")
        return True
      else:
        return False
    except Exception as err:
      print(err)

  def check_funds(self, amount):
    try:
      if amount > self.balance:
        return False
      else:
        return True
    except Exception as err:
      print(err)

def create_spend_chart(categories):
  # local vars
  total = 0.0
  max_len_of_category_names = 0
  chart_rows = [
    "100| ",
    " 90| ",
    " 80| ",
    " 70| ",
    " 60| ",
    " 50| ",
    " 40| ",
    " 30| ",
    " 20| ",
    " 10| ",
    "  0| ",
    "    -"
  ]
  for category in categories:
    # add up total cost to calculate proportions of each later
    total += category.get_total_withdrawals()
    # find longest category name
    if len(category.category) > max_len_of_category_names:
      max_len_of_category_names = len(category.category)
  # append new rows to chart_rows to make space for category names
  for new_row in range(max_len_of_category_names):
    chart_rows.append("     ")

  for category in categories:
    # find the proportion of the total for each category
    proportion = int((category.get_total_withdrawals() / total) * 10)
    # find index to start printing 'o' for chart
    start_printing_o_idx = 10 - proportion
    # concat appropriate strs to chart_row list for each category
    for row in chart_rows:
      idx = chart_rows.index(row)
      if idx >= start_printing_o_idx and idx <= 10:
        chart_rows[idx] += ("o  ")
      elif idx <= 10:
        chart_rows[idx] += ("   ")
      elif idx == 11:
        chart_rows[idx] += ("---")
      elif idx - 12 < len(category.category):
        chart_rows[idx] += (f"{category.category[idx-12]}  ")
      else:
        chart_rows[idx] += ("   ")
  # glue together pieces from chart_rows into completed return str
  res = "Percentage spent by category\n"
  for row in chart_rows:
    if chart_rows.index(row) < len(chart_rows) - 1:
      res += row + '\n'
    else:
      res += row
  return res