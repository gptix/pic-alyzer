"""Test data for pic-alyzer."""

test_single_image_msg = {
    "images": [
        {
            "image_id": 2,
            "image_url": "https://michelangelostestbucket.s3.us-west-2.amazonaws.com/b46c5e2c17813f956df74118d60cfff7",
            "category_id": 1
        }
            ]
}

test_batch_msg =  {
    "images": [{
            "image_id": 2,
            "image_url": "https://michelangelostestbucket.s3.us-west-2.amazonaws.com/b46c5e2c17813f956df74118d60cfff7",
            "category_id": 1
               },
               {
            "image_id": 42,
            "image_url": "https://michelangelostestbucket.s3.us-west-2.amazonaws.com/b46c5e2c17813f956df74118d60cfff8",
            "category_id": 13
               }
              ]        
}

foo = {
    "results": [
      {
          "image_id": 3,
          "image_url_marked_up": "https://www.dummys3url.com",
          "results": [
              {
                  "average_certainty": 82.56,
                  "count": 1,
                  "prediction": "dog",
              },
              {
                  "average_certainty": 76.22,
                  "count": 3,
                  "prediction": "zebra",
              },
          ],
      },
    ],
}
