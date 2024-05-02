from get_response import get_response
from recognition import record, recognize

if __name__ == '__main__':
    # while True:
        record()
        query = recognize()
        response = get_response(query)
        print(response)