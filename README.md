# NLP SoftK 1.1

Neste estudo, investigamos diferentes repositórios do GitHub que lidaram com modelos de machine learning aplicados aos conjuntos de dados Mypersonality.csv e Essays.csv. Esses conjuntos de dados contêm textos e rótulos binários relacionados aos traços de personalidade do Big Five.

Dentro deste repositório, construímos dois modelos, o Random Forest e o LSTM, para treinamento com esses dados. Embora ainda haja espaço para melhorias nos modelos, o Random Forest já mostrou resultados promissores o suficiente para continuarmos trabalhando nele.

## Pré-processamento

- Preparação dos dados, incluindo dividir o texto em sentenças, converter etiquetas em números, transformar sentenças em números (embeddings) e resumir o texto combinando os embeddings.

## Otimizadores e Loss (Função de Perda)

- Algoritmos para ajustar o modelo durante o treinamento e uma medida que quantifica o desempenho do modelo. Nesse caso, é usado o otimizador Adam e a função de perda binary_crossentropy.

## Evaluator (Avaliador)

- A métrica usada para medir o quão bem o modelo está se saindo. Aqui, é usada a acurácia (accuracy), que avalia com que frequência o modelo faz previsões corretas.

## Métricas

- Medidas quantitativas para avaliar o desempenho do modelo, incluindo acurácia, precisão, recall, pontuação F1 e métricas relacionadas à curva ROC e AUC (se o modelo fornecer probabilidades). A escolha das métricas depende do tipo de problema e dos objetivos de avaliação.

## Resultados

### Random Forest Essays

Accuracy: 0.058704453441295545
           precision    recall  f1-score   support
  
       cEXT       0.60      0.53      0.56       272
       cNEU       0.55      0.64      0.59       232
       cAGR       0.57      0.67      0.62       264
       cCON       0.60      0.51      0.55       267
       cOPN       0.64      0.59      0.62       267
  

micro avg 0.59 0.59 0.59 1302
macro avg 0.59 0.59 0.59 1302
weighted avg 0.59 0.59 0.59 1302
samples avg 0.57 0.58 0.54 1302


### Random Forest My Personality

Accuracy: 0.08518145161290322

            precision    recall  f1-score   support
        
       cEXT       0.52      0.14      0.22       853
       cNEU       0.62      0.05      0.09       729
       cAGR       0.58      0.68      0.63      1057
       cCON       0.56      0.28      0.38       931
       cOPN       0.76      1.00      0.86      1501
        

micro avg 0.66 0.52 0.58 5071
macro avg 0.61 0.43 0.43 5071
weighted avg 0.63 0.52 0.50 5071
samples avg 0.68 0.51 0.55 5071


## LSTM

Na pasta Documentos, temos uma análise sobre os modelos e melhorias possíveis, em conformidade com o nosso objetivo no presente momento. De modo geral, podemos concluir que quase nenhum repositório estava em perfeitas condições ou não nos atendiam no momento. Portanto, selecionamos alguns modelos e os construímos para a execução.

## Repositórios estudados:

- [https://github.com/amirmohammadkz/personality_detection](https://github.com/amirmohammadkz/personality_detection)
- [https://github.com/dbrehmer/Knowself](https://github.com/dbrehmer/Knowself)
- [https://github.com/jkwieser/personality-prediction-from-text](https://github.com/jkwieser/personality-prediction-from-text)
- [https://github.com/limyansky/Personality-Classification/blob/main/Personality_Classification.ipynb](https://github.com/limyansky/Personality-Classification/blob/main/Personality_Classification.ipynb)
- [https://github.com/yashsmehta/personality-prediction](https://github.com/yashsmehta/personality-prediction)
- [https://github.com/m43/fer-tar/tree/master](https://github.com/m43/fer-tar/tree/master)

## Créditos

Agradecemos ao Programa K (Capacitação 4.0) pela oportunidade!
