from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "BossLee/t5-gec")

beam_settings =  TTSettings(num_beams=5, min_length=1, max_length=20)
example = "grammar: This sentences, has bads grammar and spelling!"
result = happy_tt.generate_text(example, args=beam_settings)
print(result.text)