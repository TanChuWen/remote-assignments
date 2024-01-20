function max(numbers) {
    if (!numbers || numbers.length === 0) {
        return null; // Handle empty array
    }

    let maxValue = numbers[0]; // Assume the first element is the max value

    for (let i = 1; i < numbers.length; i++) {
        const num = numbers[i];
        if (num > maxValue) {
            maxValue = num;
        }
    }
    return maxValue;
}


function findPosition(numbers, target) {
    let idx = 0;
    for (const num of numbers) {
        if (target === num) {
            return idx;
        }
        idx++;
    }
    return -1;
}

// console.log(max([5,3,1]));
// console.log(max());
// console.log(max([-1,-5,-7]));

// console.log(findPosition([5,3,1,1,4],3));
// console.log(findPosition([5,3,1,1,4],1));
// console.log(findPosition([5,3,1,1,4],7));