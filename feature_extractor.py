import re

def extract_features(code: str):
    lines = code.split("\n")
    total_lines = max(len(lines), 1)
    non_empty_lines = [l for l in lines if l.strip()]

    # 1. Comment ratio
    comments = len([l for l in lines if l.strip().startswith("#")])
    comment_ratio = comments / total_lines

    # 2. Long lines (>80 chars)
    long_lines = len([l for l in lines if len(l) > 80])

    # 3. Nesting depth using { } and indentation
    depth = 0
    max_depth = 0
    for l in lines:
        depth += l.count("{") - l.count("}")
        max_depth = max(max_depth, depth)
    
    # Also check Python-style indentation depth
    python_depth = 0
    for l in non_empty_lines:
        indent = len(l) - len(l.lstrip())
        python_depth = max(python_depth, indent // 4)  # Assuming 4 spaces per indent
    max_depth = max(max_depth, python_depth)

    # 4. Bad variable names (single letters)
    bad_names = len(re.findall(r"\b[a-z]\b", code))

    # 5. Function length estimation
    functions = re.findall(r"def .*?:", code)
    function_count = len(functions)

    # 6. Average line length
    if non_empty_lines:
        avg_line_length = sum(len(l) for l in non_empty_lines) / len(non_empty_lines)
    else:
        avg_line_length = 0

    # 7. Whitespace ratio (empty lines)
    empty_lines = len([l for l in lines if not l.strip()])
    whitespace_ratio = empty_lines / total_lines if total_lines > 0 else 0

    # 8. Import count
    imports = len(re.findall(r"^(import|from)\s+", code, re.MULTILINE))

    # 9. Docstring presence (simple check)
    has_docstring = 1 if re.search(r'""".*?"""', code, re.DOTALL) or re.search(r"'''.*?'''", code, re.DOTALL) else 0

    # 10. Cyclomatic complexity (simple: count if/elif/else/for/while/try/except)
    complexity_keywords = len(re.findall(r'\b(if|elif|else|for|while|try|except|with)\b', code))

    return {
        "lines": total_lines,
        "comment_ratio": round(comment_ratio, 2),
        "long_lines": long_lines,
        "max_depth": max_depth,
        "bad_names": bad_names,
        "function_count": function_count,
        "avg_line_length": round(avg_line_length, 2),
        "whitespace_ratio": round(whitespace_ratio, 2),
        "import_count": imports,
        "has_docstring": has_docstring,
        "complexity": complexity_keywords
    }
