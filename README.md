# Azure AI Document Intelligence
Stosunkowo nowe i zbierające bardzo dobre odnośnie skuteczności opinie rozwiązanie microsoftu. 

Rozwiązanie posiada następujące zalety:
- Cloud base
- Łatwa implementacja - kod w pliku azure_di.py wymaga domeny i klucza do zasobu + jednej libki:
```
pip install azure-ai-documentintelligence==1.0.0b2
```
- free tier 500 stron/month (trzeba mieć konto w azure z podpiętą kartą) - jest to na tyle dużo, że dla odpowiednio małych projektów, może się okazać wystarczająco; pózniej 1,5$/1000 dokumentów

Dzięki dostępności free tier byłem wstanie przetestować rozwiązanie na przykładowej etykiecie corello.pdf, wynik można zobaczyć w Corello_azure.md

Ciekawym przykładem jest fragment pdf, w którym 



