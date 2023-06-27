def arithmetic_arranger(problems, solution = False):
    valid_operators = ["+", "-"]
    # checking for invalid states
    if len(problems) > 5:
        return "Error: Too many problems"
    for problem in problems:
        parts = problem.split(" ")
    if parts[1] not in valid_operators:
        return "Error: Operator must be '+' or '-'."
    if len(parts[0]) > 4 or len(parts[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
    if parts[0].isdigit() == False or parts[2].isdigit() == False:
        return "Error: Numbers must only contain digits."
    
    # arranging the problems

    arranged_problems = []
    top_lines = []
    bottom_lines = []
    result_lines = []
    line_lines = []

    for problem in problems:
        parts = problem.split(" ")
        width = max(len(parts[0]), len(parts[2])) + 2
        top = str(parts[0]).rjust(width)
        bottom = parts[1] + str(parts[2]).rjust(width - 1)
        line = ""
        result = ""
        for s in range(width):
            line += "-"

        top_lines.append(top)
        bottom_lines.append(bottom)
        line_lines.append(line)
        lines = []

        if solution:
            if parts[1] == "+":
                result = str(int(parts[0]) + int(parts[2])).rjust(width)
            else:
                result = str(int(parts[0]) - int(parts[2])).rjust(width)
            result_lines.append(result)
    
    lines.append("    ".join(top_lines))
    lines.append("    ".join(bottom_lines))
    lines.append("    ".join(line_lines))
    
    if solution:
        lines.append("    ".join(result_lines))
    
    return "\n".join(lines)


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49777" ], solution = True))