import csv


def main():
    with open('input.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        ncol = len(next(csv_reader))

    f_out = open('output.txt', 'w')

    f_out.write("\\begin{table}[!hbtp]\n"
                "\t\\centering\n"
                "\t\\begin{tabular}{%s}\n" % ' '.join('c'*ncol))
    f_out.write("\t\t\\hline\n")

    with open('input.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')

        f_out.write("\t\t%s\\\\\n" % " & ".join(next(csv_reader)))
        f_out.write("\t\t\\hline\n")

        for row in csv_reader:
            f_out.write("\t\t%s\\\\\n" % " & ".join(row))

    f_out.write("\t\t\\hline\n"
                "\t\\end{tabular}\n"
                "\t\\caption{Caption}\n"
                "\t\\label{Tab:Label}\n"
                "\\end{table}\n"
                )

    f_out.close()


if __name__ == '__main__':
    main()
