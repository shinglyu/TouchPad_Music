function apply2score(nmat, score)
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
   if (size(nmat, 1) != size(score, 1))
      warning('The recording doesn\'t match the length of the score, please re-record it.' )
   else 
      score(:, S_VELOCITIES) = namt(:, N_VELOCITIES);
      score(:, S_ONSET_SEC) = namt(:, N_ONSET_SEC);
      score(:, S_DURATION_SEC) = namt(:, N_DURATION_SEC);
   end
   %TODO: write midi
end
