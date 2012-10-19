function outScore = apply2score(nmat, score, scoreName)
   assert(size(nmat, 2) == 4);
   N_VELOCITIES     = 1;
   N_ONSET_SEC      = 2;
   N_DURATION_SEC   = 4;

   S_ONSET_BEATS    = 1;
   S_DURATION_BEATS = 2;
   S_CHANNELS       = 3;
   S_PITCHS         = 4;
   S_VELOCITIES     = 5;
   S_ONSET_SEC      = 6;
   S_DURATION_SEC   = 7;
   if (size(nmat, 1) ~= size(score, 1))
      warning(['The recording length(' num2str(size(nmat, 1)) ') not matching the score length (' num2str(size(score, 1)) '), please re-record it.'] )
      outScore = [];
   else 
      score(:, S_VELOCITIES) = nmat(:, N_VELOCITIES);
      score(:, S_ONSET_SEC) = nmat(:, N_ONSET_SEC);
      score(:, S_DURATION_SEC) = nmat(:, N_DURATION_SEC);
      outScore = score;
   end
end
