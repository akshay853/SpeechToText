import deepspeech

model_file_path = 'models/deepspeech-0.9.3-models.pbmm'
model = deepspeech.Model(model_file_path)

scorer_file_path = 'models/deepspeech-0.9.3-models.scorer'
model.enableExternalScorer(scorer_file_path)

lm_alpha = 0.75
lm_beta = 1.85

#lm_alpha = 0.931289039105002
#lm_beta = 1.1834137581510284
model.setScorerAlphaBeta(lm_alpha, lm_beta)

beam_width = 200

model.setBeamWidth(beam_width)