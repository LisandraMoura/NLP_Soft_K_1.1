# NLP_Soft_K_1.1


Ao longo desse estudo exploramos vários repositórios do GitHub que trabalharam com modelos de machine learning aplicados aos conjuntos de dados Mypersonality.csv e Essays.csv.
Os dois datasets trazem textos e anotações binárias sobre os traços de personalidade do Big Five. Neste repositório construimos dois modelos para serem treinados com os datasets, Randon Forest e LSTM. Ainda é necessário otimizações e provavelmente uma melhoria nos modelos, mas com o randon forest já conseguimos resultados satisfatórios para continuar.


-- Pr-processamento
-- Otimizadores e loss
-- Evaluator 
-- Metricas

--  Randon Forest Essays

      Accuracy: 0.058704453441295545
                    precision    recall  f1-score   support
      
              cEXT       0.60      0.53      0.56       272
              cNEU       0.55      0.64      0.59       232
              cAGR       0.57      0.67      0.62       264
              cCON       0.60      0.51      0.55       267
              cOPN       0.64      0.59      0.62       267
      
         micro avg       0.59      0.59      0.59      1302
         macro avg       0.59      0.59      0.59      1302
      weighted avg       0.59      0.59      0.59      1302
       samples avg       0.57      0.58      0.54      1302


-- Randon Forest My Personality


            Accuracy: 0.08518145161290322
                          precision    recall  f1-score   support
            
                    cEXT       0.52      0.14      0.22       853
                    cNEU       0.62      0.05      0.09       729
                    cAGR       0.58      0.68      0.63      1057
                    cCON       0.56      0.28      0.38       931
                    cOPN       0.76      1.00      0.86      1501
            
               micro avg       0.66      0.52      0.58      5071
               macro avg       0.61      0.43      0.43      5071
            weighted avg       0.63      0.52      0.50      5071
             samples avg       0.68      0.51      0.55      5071

-- LSTM

Na pasta Documentos temos uma analise sobre os modelos e melhorias possíveis, em conformidade com o nosso objetivo no presente momento. De modo geral, podemos concluir que, quase nenhum repositório estava em perfeitas condições ou não nos atendiam no momento. Portanto, selecionamos alguns modelos e o construimos para a execução. 


# Repositórios estudados:


https://github.com/amirmohammadkz/personality_detection


https://github.com/dbrehmer/Knowself


https://github.com/jkwieser/personality-prediction-from-text


https://github.com/limyansky/Personality-Classification/blob/main/Personality_Classification.ipynb


https://github.com/yashsmehta/personality-prediction


https://github.com/m43/fer-tar/tree/master



## Créditos

Agradecemos ao Programa K (Capacitação 4.0) pela oportunidade!
