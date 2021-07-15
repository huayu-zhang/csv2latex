# Simple script to convert csv to latex table

## To use

Copy csv text to `input.csv`

For example

```csv
a,b,c
1,2,3
4,5,6
7,8,9
```

Run main.py

```bash
python3 main.py
```

See the output in `output.txt`

```latex
\begin{table}[!hbtp]
	\centering
	\begin{tabular}{c c c}
		\hline
		a & b & c\\
		\hline
		1 & 2 & 3\\
		4 & 5 & 6\\
		7 & 8 & 9\\
		\hline
	\end{tabular}
	\caption{Caption}
	\label{Tab:Label}
\end{table}
```
