# Simple Logo Detection Google Vision API Test

```
pip install requests
export TOKEN=$(gcloud auth print-access-token)
python LogoDetection.py
```

You will then see results start to show up. 

```
C02J41R5DKQ4:logo-detection-test jkurz$ python LogoDetection.py
1.-toyota-logo2.jpg : Toyota : 0.34892106
1280px-Reddit_logo_and_wordmark.svg.png : reddit : 0.55927235
1427229210313.jpg : Chevrolet : 0.8262858
3038581_orig.jpg : No Results
7dc3a1bda74a85eb325b902bd5eb53c5--corporate-style-corporate-logos.jpg : Nivea : 0.54253477
Adidas.png : Adidas : 0.61623347
amazon-com-logo.jpg : Amazon Payments : 0.41740993
Android-Company-Logo.jpg : Android : 0.37905684
apple-nike-fedex-logos.png : FedEx : 0.31642407
apple.jpg : No Results
apple.png : No Results
beats-logo-1200-80.jpg : No Results
bmw_logo_79.jpg : BMW : 0.60142285
Cartoon-Network-logo-2004-1024x768.png : Cartoon Network : 0.5042324
```


After it's done it will write to `./results` a csv of the run.

### Questions

* Why are the confidence scores so low?
* Why does it not get seemingly simple logos like nike?
* If the confidence level is so low, how are we expected to know what is false positive and what is not?
* Is there any suggestion to make this more accurate?
* Is there any way to help the models get better for false positives or false negatives we see?
