# Simple Logo Detection Google Vision API Test

```
pip install requests
export TOKEN=$(gcloud auth print-access-token)
python LogoDetection.py
```

You will then see results start to show up. After it's done it will write to `./results` a csv of the run.

Here is a list, sorted on confidence, of those results. Taken on 2017-08-29

#### Results

```
ImagName                                Logo                Confidence
pringles+moustache+logo.jpeg            Pringles            0.835251
1427229210313.jpg                       Chevrolet           0.8262858
Rolex-Logo-Font.jpg                     Rolex               0.7227277
playstation-logo.jpg                    PlayStation         0.7101602
cartoonnetwork.png                      Cartoon Network     0.6752881
Adidas.png                              Adidas              0.61623347
slack-logo-vector-download.jpg          Slack               0.6067425
bmw_logo_79.jpg                         BMW                 0.60142285
main-desktop-browser-logos.png          Firefox             0.5664752
lyft.jpg                                Lyft                0.5655652
1280px-Reddit_logo_and_wordmark.svg.png reddit              0.55927235
7dc3a1bda74a85eb325b902bd5eb53c5--corporate-style-corporate-logos.jpg   Nivea   0.54253477
WhatsApp-logo-as.png                    Whatsapp                0.5146856
Cartoon-Network-logo-2004-1024x768.png  Cartoon Network             0.5042324
Olympic-logo.png                        Olympic Games               0.47975618
pepsi.png                               Pepsi               0.46848878
hqdefault.jpg                           Coca-Cola               0.44611672
youtube-logo-preview-1.png              YouTube             0.43424568
amazon-com-logo.jpg                     Amazon Payments             0.41740993
exterior-view-of-football-or-soccer-stadium-on-july-26-2015-in-son-F06D1Y.jpg   Coca-Cola   0.41034395
turner_logo_detail.png                  Download                0.40681517
google.png                              Google              0.40530983
Swatch-Logo-logotype-1024x768.png       Swatch              0.40468112
youtube_logo_detail.png                 YouTube             0.39970717
scenes-from-around-the-beautiful-new-yankee-stadium-in-the-bronx-bx415d.jpg Bank of America 0.39590633
Android-Company-Logo.jpg                Android             0.37905684
Logo Puma 10.jpg                        Puma                0.35380706
1.-toyota-logo2.jpg                     Toyota              0.34892106
Mercedes-symbol.jpg                     Mercedes-Benz Bank  0.3183524
apple-nike-fedex-logos.png              FedEx               0.31642407
CNN-Travel-logo.png                     Burson-Marsteller   0.29273647
TURNER_NEW_LOGO.png                     Turner Broadcasting System  0.25683364
lg.jpg                                  Apple               0.22079897
cartoonnetwork.png                      Cartoon Network     0.20921344
scenes-from-around-the-beautiful-new-yankee-stadium-in-the-bronx-bx415d.jpg Delta   0.16433412
scenes-from-around-the-beautiful-new-yankee-stadium-in-the-bronx-bx415d.jpg Tradepoint  0.14830595
cartoonnetwork.png                      Cartoon Network Block Party 0.06261815
```

#### No Results for these images

```
3038581_orig.jpg         
apple.jpg        
apple.png        
beats-logo-1200-80.jpg       
DSC_03332.jpg        
ig-logo-email.png        
led-smd-perimeter-advertising-screens-football-stadiums.jpg      
logo.jpg         
McDonald's_(2003).gif        
Nike.jpg         
pepsi.jpg        
stadium1.jpg         
subway.jpg       
pringles+mo
```

### Questions

* Why are the confidence scores so low?
* Why does it not get seemingly simple logos like nike?
* If the confidence level is so low, how are we expected to know what is false positive and what is not?
* Is there any suggestion to make this more accurate?
* Is there any way to help the models get better for false positives or false negatives we see?
