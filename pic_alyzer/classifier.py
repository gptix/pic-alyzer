## This function is a dummy, until DS9 provides function that will provide response.
def img_pred(path):
    """Sends a path to an image to the classifier, should return a
    JSON object."""
    result = {
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

    return result


def image_dict_to_response(image_dict):
    """Get prediction for one image, return in expected dict format."""
    return {'image_id' : image_dict['image_id'], 
            'result': img_pred(image_dict['image_url'])}


def batch_to_response_set(batch):
    """Get predictions for a batch of images, return as JSON object"""

    return {
        'results' : list(map(image_dict_to_response, batch))
            }
