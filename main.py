import pandas as pd
indices = [4, 5, 8, 9, 13, 17, 18, 19, 20, 21, 22, 23, 24, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 58, 61, 62, 79, 80, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 105, 106, 107, 116, 117]
y_index = 111


def read_xlsx(file_path='t1.xlsx'):
    data = pd.read_excel(file_path)
    nuks = data.iloc[:, y_index]
    related_indices = []
    for i, n in enumerate(nuks):
        if n == '-':
            pass
        else:
            related_indices.append(i)
    final_data = []
    for ind in indices:
        datum = data.iloc[:, ind]
        final_datum = []
        for r_ind in related_indices:
            final_datum.append(datum[r_ind])
        final_data.append(final_datum)
    return final_data


if __name__ == '__main__':
    d = read_xlsx()
    print(d)
