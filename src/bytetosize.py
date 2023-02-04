import math
def bytes_to_size(bytes: int) -> str:
        sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', "PB", "EB", "ZB", "YB"]

        # Check for zero
        if bytes == 0:
            return 'n/a'

        # Get the index of the appropriate size
        i = int(math.floor(math.log(abs(bytes)) / math.log(1024)))

        # Check if the index is zero
        if i == 0:
            return f"{bytes} {sizes[i]}"

        # Convert the bytes to the appropriate size
        return f"{(bytes / (1024 ** i)):.1f} {sizes[i]}"