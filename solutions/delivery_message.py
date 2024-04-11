from typing import List


def delivery_message(timestamps: List[int], messages: List[str], k: int) -> List[bool]:
    result: List[bool] = []
    last_delivered: dict[str, int] = {}

    for i in range(len(timestamps)):
        timestamp = timestamps[i]
        message = messages[i]

        if message in last_delivered and timestamp - last_delivered[message] < k:
            result.append(False)
        else:
            result.append(True)
            last_delivered[message] = timestamp

    return result
