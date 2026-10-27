def build_sales_report(raw: str) -> str:
    """
    `raw` is multi-line text. Each meaningful line has the form
        item , quantity , price
    with arbitrary whitespace around each field.

    Processing rules, applied to every line from splitlines():
      1. Strip the line. Skip it if it is empty or starts
         with "#".
      2. Split on "," . Skip the line if it does not have
         exactly 3 fields.
      3. Strip each field. Skip the line if the quantity field
         is not made only of digits. Convert quantity with
         int() and price with float().
      4. Format the item as title case, truncated to at most 12
         characters (slice AFTER applying title case).
      5. line_total = quantity * price.

    Build these output lines, in order, joined by "\\n" with
    no trailing newline:
      - Header: f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}"
      - One row per valid record, in input order:
          item (width 12, left), quantity (width 4, right),
          price (width 10, right, 2 decimals),
          line_total (width 12, right, 2 decimals, with
          thousands separators)
      - A separator line of 38 "-" characters (use *).
      - Grand total line: "TOTAL" left-aligned in width 26,
        then the sum of all line totals right-aligned in width
        12 with 2 decimals and thousands separators.
      - Summary line:
          f"Rows: {rows} | UTF-8 bytes in items: {bytes_total}"
        where `bytes_total` is the sum of the UTF-8 byte lengths
        of the formatted (title-cased, truncated) item labels.

    If there are no valid records, the report still contains the
    header, separator, a grand total of 0.00, and the summary
    with Rows: 0 and 0 bytes.
    """

    lines = raw.splitlines()
    # print("Raw:") 
    # print(raw)
    # print()

    # item (width 12, left), quantity (width 4, right),
    #       price (width 10, right, 2 decimals),
    #       line_total (width 12, right, 2 decimals, with
    #       thousands separators)

    SUM_TOTAL = 0.0
    rows = 0
    bytes_total = 0
    
    Answer_list = []
    Answer_list.append(f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}")
    for line in lines:
        if(len(line) != 0 and not(line.startswith("#"))):
            line = line.strip()
            # print(line)

            split_list = line.split(',')
            # print(split_list)
            if(len(split_list) == 3):
                field_1 = split_list[0].strip()
                field_2 = split_list[1].strip()
                field_3 = split_list[2].strip()

                # print(field_2)
                is_dec = 1
                for char in field_2:
                    if(ord(char) < 48 or ord(char) > 57):
                        is_dec = 0

                if(is_dec):
                    ITEM = field_1.title()[:12]
                    QTY = int(field_2)
                    PRICE = float(field_3)
                    TOTAL = QTY* PRICE
                    
                    Answer_list.append(f"{ITEM:<12}{QTY:>4}{f"{PRICE:.2f}":>10}{f"{TOTAL:,.2f}":>12}")
                    SUM_TOTAL += TOTAL
                    rows += 1 
                    bytes_total += len(ITEM.encode("utf-8"))
            # print()
                
    separator_line = f"{"-"*38}"
    Answer_list.append(separator_line)
    total_line = f"{"TOTAL":<26}{f"{SUM_TOTAL:,.2f}":>12}"
    summary_line = f"Rows: {rows} | UTF-8 bytes in items: {bytes_total}"
    Answer_list.append(total_line)
    Answer_list.append(summary_line)

    # print("Pen\n2342")
    # print(Answer_list)
    ans = '\n'.join(Answer_list)
    print(ans)
    
    return ans
