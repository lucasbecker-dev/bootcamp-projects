import re

def arithmetic_arranger(problems, display_answers=False):
  # Assert no more than 5 problem strings passed in
  num_problems = len(problems)
  if num_problems > 5:
    return 'Error: Too many problems.'
  # Initialize local vars
  operator_regex = '^[+-]$'
  operand_digits_regex = '^\d+$'
  operand_length_regex = '^\d{1,4}$'
  space_between_problems = '    '
  arranged_problems_list = ['', '', '']
  if (display_answers == True):
    arranged_problems_list.append('')
  arranged_problems = ''
  # Split each problem into its constituent elements
  for problem in problems:
    elements = problem.split()
    # Cache appropriately named references to each element for clarity
    l_operand = elements[0]
    operator = elements[1]
    r_operand = elements[2]

    # Assert operator is + or -
    if not re.match(operator_regex, operator):
      return 'Error: Operator must be \'+\' or \'-\'.'
    # Assert operands contain only digits
    if not re.match(operand_digits_regex, l_operand) or not re.match(operand_digits_regex, r_operand):
      return 'Error: Numbers must only contain digits.'
    # Assert operands are no more than 4 digits in length
    if not re.match(operand_length_regex, l_operand) or not re.match(operand_length_regex, r_operand):
      return 'Error: Numbers cannot be more than four digits.'
    
    # Determine width of this problem for output purposes
    problem_width = 2 + max(len(l_operand), len(r_operand))
    # Write top row
    for elem in range(problem_width - len(l_operand)):
      arranged_problems_list[0] += ' '
    arranged_problems_list[0] += l_operand + space_between_problems
    # Write middle row
    arranged_problems_list[1] += operator
    for elem in range(problem_width - 1 - len(r_operand)):
      arranged_problems_list[1] += ' '
    arranged_problems_list[1] += r_operand + space_between_problems
    # Write equals line row
    for elem in range(problem_width):
      arranged_problems_list[2] += '-'
    arranged_problems_list[2] += space_between_problems
    # If display_answers is True, write answer row
    if (display_answers == True):
      if (operator == '+'):
        answer = int(l_operand) + int(r_operand)
      else:
        answer = int(l_operand) - int(r_operand)
      for i in range(problem_width - len(str(answer))):
        arranged_problems_list[3] += ' '
      arranged_problems_list[3] += str(answer) + space_between_problems
  
  # Join answer strings together
  arranged_problems += arranged_problems_list[0].rstrip() + '\n' + arranged_problems_list[1].rstrip() + '\n' + arranged_problems_list[2].rstrip()
  if (len(arranged_problems_list) > 3):
    arranged_problems += '\n' + arranged_problems_list[3].rstrip()


  return arranged_problems