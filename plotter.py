import matplotlib.pyplot as plt

def plotter(line_data, title, x_label, y_label, filename):
    # line_data: [{line_name, x_data, y_data}]

    colors = ['red', 'green', 'blue']
    plt.figure(figsize=(15, 15))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.xticks(rotation=-45)

    for i in range(len(line_data)):
        data = line_data[i]
        color = colors[i % 3]
        line_name = data.get('line_name')
        x_data = data.get('x_data')
        y_data = data.get('y_data')
        plt.plot(x_data, y_data, label=line_name, color=color, marker='o', linestyle='-')

    plt.legend()
    plt.savefig(filename)
