def main(nums):
    Checked = set()
    Results = []
    for num in nums:
        if num not in Checked:
            Results.append(num)
            Checked.add(num)
    return Results

nums = [3,5,3,1]
print(main(nums))