Image Optical Character Recognition API will help you categorize the place where the scene happens in the provided picture using Deep Learning technics

Read these papers to learn more about this technic:
[Font and Background Color Independent Text Binarization](http://mile.ee.iisc.ernet.in/publications/softCopy/DocumentAnalysis/CBDAR_Kasar_2007.pdf)

```
@inproceedings{Kasar2007FontAB,
  title={Font and Background Color Independent Text},
  author={T. Kasar and Jai Kumar and A. G. Ramakrishnan},
  year={2007}
}
```

- - -
EXAMPLE
![output](https://i.ibb.co/PN7jYL6/example.png)
- - -
INPUT

```json
{
  "url": "https://i.ibb.co/TwWWp22/input.jpg"
}
```
- - -
EXECUTION
```bash
curl -X POST "https://api-market-place.ai.ovh.net/image-scene-recognition/detect" -H "accept: application/json" -H "X-OVH-Api-Key: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" -H "Content-Type: application/json" -d "{\"url\":\"https://i.ibb.co/TwWWp22/input.jpg\"}"
```
- - -

OUTPUT

```json
[
  {
    "type":"default",
    "text":"APOLLO 13 MISSION COMMENTARY 4-12-70 CST $:04P GET 27:51 85/1\n\nse Hello Houston, Apollo 13.\nCAPCOM 13, Houston. Go ahead.\nsc Just a passing comment Joe, we're having lunch\n\nright now and I just made myself a hot dog sandwich with\ncatsup. Very tasty and almost unheard of in the old days.\n\nCAPCOM that\u2019s correct 13, As I recall the flight\nplan, you're suppose to put mustard on the hot dogs and not\ncatsup but I guess we'll overlook that.\n\nsc We blew it.\n\nsc Right.\n\nCAPCOM How's everything going?\n\nsc About pretty good. We have about 4 different\nmethods of spreading catsup, right nov.\n\nCAPCOM = Okay, Jack. We'll have your update to you\nbefore too long.\n\nsc Okay, fine Joe. We did a pit check on the\nHycon camera and everything works okay.\n\nCAPCOM Okay. Beautiful. We don't have anything else\n\nfor you at the moment.\n\nEND OF TAPE"
  },
  {
    "type":"denoising",
    "text":"APOLLO 13 MISSION COMMERTARY 4-12-70 CST S:04P CET 27:51 85/1\n\nsc Hello Houston, Apollc 13.\nCAPCOM 13, Houaton. Go ahead.\nsc Just a pausing comeent Joe, we're having lunch\n\n   \n\nright nov and I just aade eyself a hot dog sandvich vith\ncatsup. ry Canty and aleost unheard of in the old days.\n\nCAPCOM = That'a correct 13, Aw I recall the flight\nplan, you're suppose to put avetard oo the hot dogs and not\ncatsup but 1 guesa ve'll overlook thar.\n\n   \n\n \n\nse We blew te.\n\nsce Right.\n\nCAPCOM == How's everything going?\n\nsc About pretty good, Se have about 4 dt fferent\neethods of spreading catsup, right now.\n\nCAPCOM = Okay, Jack. LL Nave your update to you\nbefore too lone.\n\nse Okay, fine Joe, ie did # pit check on the\nNycon camera and everything works okay.\n\nCAPCOM Okay. Beautitul. We don't have anything elac\n\nfor you at the eooent.\n\nEND OF TAPE"
  }
]
```

please refer to swagger documentation for further technical details: [swagger documentation](https://market-place.ai.ovh.net/#!/apis/0cdfb0df-2aff-45fb-9fb0-df2affe5fb19/pages/f791f3f7-3fdb-40df-91f3-f73fdb10df54)

* * *
<div>Icons made by <a href="https://www.flaticon.com/authors/mynamepong" title="mynamepong">mynamepong</a> from <a href="https://www.flaticon.com/"           title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/"          title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>