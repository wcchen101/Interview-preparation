class Solution():
    def bucketSort(self, Arr):
        result = []
        if Arr is None:
            return result

        # 1. Create bucket container list
        container = [[] for _ in range(len(Arr))]

        # 2. Add corresponding item into certain bucket
        for item in Arr:
            val_int = int(item * len(Arr))
            container[val_int].append(item)

        # 3. Sort each bucket
        for bucket in container:
            bucket.sort()

        # 4. Collect the sorted element from sorted bucket, and put into the final result
        for bucket in container:
            for item in bucket:
                result.append(item)

        return result

