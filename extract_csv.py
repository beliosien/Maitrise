import csv


def extract_name(project):
    arr = project.split("/")

    if arr[0] == ".":
        return arr[1]

    return arr[0]


def extract_csv(csv_file):
    assert csv_file is not None, 'csv file must not be none'
    table = dict()
    duplicate = dict()

    with open(csv_file, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            project, code, lines, test, rule = row

            if (project, code, lines, test, rule) not in duplicate.keys():
                duplicate[(project, code, lines, test, rule)] = 1
            else:
                duplicate[(project, code, lines, test, rule)] += 1
    file.close()

    count = 0
    for row in duplicate.keys():
        project, code, lines, test, rule = row
        if test == "1" and 'pre-commit-hooks.git' in project and rule == "F2L.5":
            count += 1
            print(project, code, lines, test, rule)

    print(count)


    '''for row in duplicate.keys():
        project, code, lines, test, rule = row

        name = extract_name(project=project)

        if test == "1":
            if name in table.keys():
                if rule == "F2L.1":
                    table[name][0] += 1
                elif rule == "F2L.2":
                    table[name][1] += 1
                elif rule == "F2L.3":
                    table[name][2] += 1
                elif rule == "F2L.4":
                    table[name][3] += 1
                elif rule == "F2L.5":
                    table[name][4] += 1
            else:
                if rule == "F2L.1":
                    table[name] = [1, 0, 0, 0, 0]
                elif rule == "F2L.2":
                    table[name] = [0, 1, 0, 0, 0]
                elif rule == "F2L.3":
                    table[name] = [0, 0, 1, 0, 0]
                elif rule == "F2L.4":
                    table[name] = [0, 0, 0, 1, 0]
                elif rule == "F2L.5":
                    table[name] = [0, 0, 0, 0, 1]
        else:
            if name not in table.keys():
                table[name] = [0, 0, 0, 0, 0]'''

    return table


def write_row_in_csv(filename, row=[]):
    """write a row in the specified filename"""
    f = open(filename, "a")
    writer = csv.writer(f)

    # write the data
    if len(row) > 0:
        writer.writerow(row)
    f.close()


def main():
    table = extract_csv(csv_file="./parsed.csv")
    filename = "results_rules.csv"
    for project, rules in table.items():
        row = [project] + rules
        write_row_in_csv(filename=filename, row=row)
    print("done")


if __name__ == '__main__':
    main()
