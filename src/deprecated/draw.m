data = importdata('record_0.txt.processed.csv')
plot(data(:, 1), data(:, 2));
stairs(data(:, 1), data(:, 2));
