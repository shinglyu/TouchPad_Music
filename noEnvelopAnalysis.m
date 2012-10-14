data = importdata('record_0.txt.processed.csv')

TIME = 1;
PRESSURE = 2;
MULTI= 3;
%onset = (data(:, PRESSURE)>0) && [0; data(1: end-1, PRESSURE)] == 0); % 0-> bigger than 0
multi = data(:, MULTI) - [0; data(1:end-1, MULTI)];
queue = {};
nmat = []; %pressure, onset,  off, dura
for (t = 1: size(multi, 1))
   if (multi(t) > 0) 
      queue{end + 1} = [data(t, PRESSURE) data(t, TIME)];
      
      disp(queue)
   elseif (multi(t) < 0 )
      dura = data(t, TIME) - queue{1}(2);
      nmat = [nmat; queue{1}, data(t, TIME), dura];
      queue(1) = [];
   end
end   
disp(nmat)
   
c = {'r', 'm', 'b'}
for (t = 1:size(nmat, 1))
   timeRange = (nmat(t,2): 0.001:nmat(t,3));
   pressure = nmat(t, 1) * ones(size(timeRange));
   plot(timeRange, pressure, 'x', 'color', c{mod(t, 3)+1});
   hold on;
end
%plot(data(:, 1), data(:, 2));
%stairs(data(:, 1), data(:, 2));
