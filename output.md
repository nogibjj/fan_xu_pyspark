# NBA Stats Analysis

## Data Loading

Data loaded successfully.

## Data Exploration

### First 3 Rows

|   Rk | Player                |   Age | Team   | Pos   |   G |   GS |   MP |   FG |   FGA |   FG% |   3P |   3PA |   3P% |   2P |   2PA |   2P% |   eFG% |   FT |   FTA |   FT% |   ORB |   DRB |   TRB |   AST |   STL |   BLK |   TOV |   PF |   PTS | Awards                   |
|-----:|:----------------------|------:|:-------|:------|----:|-----:|-----:|-----:|------:|------:|-----:|------:|------:|-----:|------:|------:|-------:|-----:|------:|------:|------:|------:|------:|------:|------:|------:|------:|-----:|------:|:-------------------------|
|    1 | Joel Embiid           |    29 | PHI    | C     |  39 |   39 | 33.6 | 11.5 |  21.8 | 0.529 |  1.4 |   3.6 | 0.388 | 10.2 |  18.3 | 0.556 |  0.561 | 10.2 |  11.6 | 0.883 |   2.4 |   8.6 |  11   |   5.6 |   1.2 |   1.7 |   3.8 |  2.9 |  34.7 | AS                       |
|    2 | Luka Dončić           |    24 | DAL    | PG    |  70 |   70 | 37.5 | 11.5 |  23.6 | 0.487 |  4.1 |  10.6 | 0.382 |  7.4 |  13   | 0.573 |  0.573 |  6.8 |   8.7 | 0.786 |   0.8 |   8.4 |   9.2 |   9.8 |   1.4 |   0.5 |   4   |  2.1 |  33.9 | MVP-3CPOY-6ASNBA1        |
|    3 | Giannis Antetokounmpo |    29 | MIL    | PF    |  73 |   73 | 35.2 | 11.5 |  18.8 | 0.611 |  0.5 |   1.7 | 0.274 | 11   |  17.1 | 0.645 |  0.624 |  7   |  10.7 | 0.657 |   2.7 |   8.8 |  11.5 |   6.5 |   1.2 |   1.1 |   3.4 |  2.9 |  30.4 | MVP-4DPOY-9CPOY-12ASNBA1 |

### Total Number of Observations/Rows: 739

### Summary Statistics

| summary   |       Age |       AST |        STL |
|:----------|----------:|----------:|-----------:|
| count     | 735       | 735       | 735        |
| mean      |  26.1551  |   1.93415 |   0.587347 |
| stddev    |   4.37174 |   1.80025 |   0.393774 |
| min       |  19       |   0       |   0        |
| max       |  39       |  10.9     |   2.1      |

## SQL Queries

### Top 10 Highest Scoring Players

| Player                  | Team   | Pos   |   PTS |
|:------------------------|:-------|:------|------:|
| Joel Embiid             | PHI    | C     |  34.7 |
| Luka Dončić             | DAL    | PG    |  33.9 |
| Giannis Antetokounmpo   | MIL    | PF    |  30.4 |
| Shai Gilgeous-Alexander | OKC    | PG    |  30.1 |
| Jalen Brunson           | NYK    | PG    |  28.7 |
| Devin Booker            | PHO    | PG    |  27.1 |
| Kevin Durant            | PHO    | PF    |  27.1 |
| Jayson Tatum            | BOS    | PF    |  26.9 |
| De'Aaron Fox            | SAC    | PG    |  26.6 |
| Donovan Mitchell        | CLE    | SG    |  26.6 |

## Data Transformation

### Creating a column to calculate Assist/Turnover Ratio (1st 10 rows)

| Player                  | Team   | Pos   |   AST/TOV |
|:------------------------|:-------|:------|----------:|
| Joel Embiid             | PHI    | C     |   1.47368 |
| Luka Dončić             | DAL    | PG    |   2.45    |
| Giannis Antetokounmpo   | MIL    | PF    |   1.91176 |
| Shai Gilgeous-Alexander | OKC    | PG    |   2.81818 |
| Jalen Brunson           | NYK    | PG    |   2.79167 |
| Devin Booker            | PHO    | PG    |   2.65385 |
| Kevin Durant            | PHO    | PF    |   1.51515 |
| Jayson Tatum            | BOS    | PF    |   1.96    |
| De'Aaron Fox            | SAC    | PG    |   2.15385 |
| Donovan Mitchell        | CLE    | SG    |   2.17857 |

