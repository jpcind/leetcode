def max_sum(nums):
    new_list = []
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        for j in range(len(nums)+1):
            if j <= i:
                continue
            new_list.append(sum(nums[i:j]))
    return max(new_list)

def max_sub_array(nums):
    maxSub = nums[0]
    curSum = 0
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub





def main():
    my_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    my_list2 = [2, 0, 5, 8, 23, 50, -17, 2, -103, 3]
    my_list3 = [5, 4, -1, 7, 8]
    my_list4 = [-2, -1]
    my_list5 = [-57,9,-72,-72,-62,45,-97,24,-39,35,-82,-4,-63,1,-93,42,44,1,-75,-25,-87,-16,9,-59,20,5,-95,-41,4,-30,47,46,78,52,74,93,-3,53,17,34,-34,34,-69,-21,-87,-86,-79,56,-9,-55,-69,3,5,16,21,-75,-79,2,-39,25,72,84,-52,27,36,98,20,-90,52,-85,44,94,25,51,-27,37,41,-6,-30,-68,15,-23,11,-79,93,-68,-78,90,11,-41,-8,-17,-56,17,86,56,15,7,66,-56,-2,-13,-62,-77,-62,-12,37,55,81,-93,86,-27,-39,-3,-30,-46,6,-8,-79,-83,50,-10,-24,70,-93,-38,27,-2,45,-7,42,-57,79,56,-57,93,-56,79,48,-98,62,11,-48,-77,84,21,-47,-10,-87,-49,-17,40,40,35,10,23,97,-63,-79,19,6,39,62,-38,-27,81,-68,-7,60,79,-28,-1,-33,23,22,-48,-79,51,18,-66,-98,-98,50,41,13,-63,-59,10,-49,-38,-70,56,77,68,95,-73,26,-73,20,-14,83,91,61,-50,-9,-40,1,11,-88,-80,21,89,97,-29,8,10,-15,48,97,35,86,-96,-9,64,48,-37,90,-26,-10,-13,36,-27,-45,-3,-1,45,34,77,-66,22,73,54,11,70,-97,-81,-43,-13,44,-69,-78,30,-66,-11,-29,58,52,-61,-68,-81,25,44,-32,57,-81,66,2,52,43,35,-26,16,-33,61,-37,-54,80,-3,32,24,27,30,-69,38,-81,2,-4,47,17,5,42,-58,-51,-90,98,-33,76,-22,95,-4,89,-31,-87,-44,-69,-48,1,87,48,-90,-12,-24,39,18,-86,35,96,-14,-41,13,90,-98,32,-83,-89,7,-17,63,84,-21,-40,51,24,-51,83,31,0,-38,-5,-74,-29,59,1,87,-22,-9,-1,-49,76,57,41,44,35,-27,60,23,56,-80,-14,41,-2,22,-31,99,47,-48,7,-75,13,-97,-50,61,61,27,48,-84,94,-76,-56,70,57,84,-9,-7,-66,-49,-84,89,-29,-22,7,45,-99,75,21,24,-95,-71,48,17,-92,74,-22,45,1,-97,61,-5,-74,81,-57,83,42,33,-47,75,61,-55,41,-68,22,-51,53,-1,-99,-25,-76,-95,3,48,-1,-13,23,53,-68,-76,33,92,-4,35,50,38,18,-8,-52,47,-33,-91,91,85,-60,14,-89,93,89,-89,-55,89,92,47,38,-9,-66,-39,-79,-58,-39,53,-65,56,-11,61,-29,83,-46,19,31,-3,27,-1,-18,67,-87,-8,37,79,-20,58,68,-28,-18,-17,39,-8,43,59,33,81,13,44,37,-98,6,85,84,59,4,-8,-44,-69,91,15,74,80,83,-12,59,-37,-54,5,34,27,87,-50,-81,8,-90,52,-11,-1,-4,-97,0,78,87,-39,37,-32,30,70,-1,21,-38,-50,-22,-55,15,-85,8,60,19,-81,-35,-17,-31,-40,90,-45,-88,-44,53,-15,-41,-70,-37,-77,-33,77,-9,96,24,66,-6,85,92,72,-70,7,86,14,-32,-18,33,9,64,78,68,32,-90,57,87,62,-58,-77,68,-19,-54,-65,-42,13,-68,58,-44,25,43,-52,-26,73,55,-63,-13,-77,18,96,31,-40,51,-1,91,60,-44,55,22,-26,78,-10,32,-99,2,66,13,33,25,68,-65,-32,-84,-14,-82,70,22,5,69,-59,-22,-23,0,-70,53,-32,89,85,-77,-11,-40,77,55,68,77,-43,34,-33,66,-41,-88,-98,27,-72,-13,21,74,85,-74,21,-74,-19,97,2,10,50,46,-1,13,69,87,72,23,20,40,1,76,-49,67,43,10,79,21,-86,83,84,34,34,69,37,-45,72,-82,-70,-26,27,56,97,-97,-31,66,67,-82,-11,-13,57,66,-37,85,11,82,-5,-33,3,-15,-50,-13,95,60,-66,9,-84,-94,26,-78,-44,-70,77,-47,-90,-53,95,76,-36,-38,-60,98,-72,-21,83,15,-38,-45,81,41,16,-69,-94,11,91,-84,-79,83,-79,23,-95,-24,30,58,6,39,-95,1,-8,-54,62,31,-56,67,86,-96,-18,-75,-42,-36,66,73,-29,48,-39,-61,63,-42,98,60,81,-97,-64,11,61,18,-73,42,-80,18,87,58,-51,-69,2,-88,-66,84,-63,-32,-75,79,-82,-28,27,-21,11,-33,13,9,-73,-6,-11,-61,81,-73,57,-92,45,53,25,33,11,50,40,90,62,51,74,75,-81,75,54,-86,-53,-42,-8,34,1,-95,-79,27,-24,-14,42,-66,12,-24,-58,-66,-71,43,66,17,-29,-16,7,-90,-65,-42,84,-70,-90,15,-57,-67,49,11,67,-50,-7,64,53,68,-50,-5,78,38,71,96,71,76,40,15,-7,87,98,76,96,-90,-66,57,-61,-57,-51,-41,-47,97,69,-80,-53,-61,83,76,83,-90,-29,62,47,-81,58,18,95,-2,-67,-12,-38,-92,-35,-65,-83,-25,91,-44,-5,-83,-9,47,-86,-40,43,-63,-1,3,-87,-18,12,-39,-79,-41,-21,79,53,-26,-46,63,39,16,70,80,50,87,-45,19,-80,26,35,10,-27,26,46,92,62,-55,-5,52,4,-93,-87,1,-58,-9,-20,95,42,34,58,-19,-73,5,-39,53,-31,-8,-28,-12,95,84,97,-55,10,44,-62,-51,65,32,-99,-54,16,89,47,57,-42,-96,52,99,14,-13,-43,40,69,-6,-6,-62,85,42,26,80,26,0,-74,-87,-79,-60,-38,63,71,-61,85,-13,-71,9,-78,-14,13,50,-38,-73,-85,18,44,83,-88,-85,-79,73,56,23,31,-40,-99,33,-51,97,72,-13,60,20,26,46,84,31,-45,-94,93,67,55,-45,71,69,49,15,52,37,29,50,-13,-38,-50,-82,-2,-73,27,47,-75,-24,-66,84,96,36,7,80,-56,62,62,-63,6,17,-32,-46,-13,93,45,-84,30,-26,42,-82,13,92,-88,-89,-81,16,34,-57,91,45,-95,87,-42,11,44,2,-50,6,15,33,-76,83,86,-13,76,32,-21,-16,82,-78,-22,-28,90,-34,-40,-91,81,93,-71,73,15,-90,37,73,-3,-41,-48,47,64,66,-43,64,49,-57,-72,3,51,7,63,11,28,-82,82,18,-17,-58,3,-58,-87,8,-85,27,17,28,-23,-85,86,28,38,28,-5,94,-31,-79,-86,-3,0,65,80,-60,-24,8,-43,-65,-97,40,-23,-18,81,-11,90,72,92,-16,0,-30,-25,-36,97,-87,68,-31,83,-63,-33,97,10,66,39,-10,-93,91,74,-37,-74,53,79,-21,-64,37,67,-74,9,60,9,86,-70,84,-73,-96,73,94,-50,57,-69,16,31,18,-18,-53,-92,-35,-62,59,5,-60,12,-16,19,47,-78,-14,49,7,-77,-64,-7,-71,96,19,-67,69,-10,-18,3,-2,97,-89,-84,-44,-43,99,-2,-6,58,-97,11,-29,-14,-70,94,-16,-8,44,91,15,79,-39,20,75,57,52,21,-53,-89,-98,44,84,-88,36,-82,-31,36,15,39,-29,17,-50,41,79,-21,13,-36,71,-66,-68,-37,89,-8,82,41,-74,12,-38,-50,-1,-37,70,-39,-48,7,-22,20,-57,69,-41,13,-14,-14,-68,-58,64,21,5,12,54,13,51,43,-94,11,-16,-92,99,22,-43,-2,62,-72,58,-86,11,-87,33,53,81,68,-57,-56,-46,-49,-14,95,71,67,-16,2,-19,-87,-78,-37,0,-18,-30,-1,-95,4,96,66,31,32,79,-81,44,-11,48,3,-66,90,46,-12,-81,-91,-40,66,76,20,-54,-43,9,-33,19,-91,49,88,7,30,-8,-19,-4,99,-87,-48,-82,33,40,65,-64,73,33,59,-62,28,67,-26,-29,43,71,16,99,-20,83,18,-11,9,-16,72,-61,52,-47,34,29,-58,85,23,75,2,-34,87,-48,75,46,-33,3,-9,40,73,-66,-12,-10,-89,68,-50,5,-66,58,88,82,96,18,-64,7,-53,-23,-31,69,-71,47,-88,-83,98,86,39,-35,-34,-70,82,-60,-36,-30,6,-26,-85,55,55,-75,-10,44,84,-37,-38,-80,69,-15,-27,-85,-69,-21,61,-57,-5,59,-71,-66,-98,-5,-59,60,11,4,-93,93,54,98,48,9,99,-85,-70,83,-23,-32,79,-77,52,-47,-63,60,8,97,-97,-97,33,-92,-87,11,-21,-47,-29,66,33,-45,59,-36,-47,-16,50,-48,-2,79,-64,51,-75,-85,73,76,-56,-90,13,51,83,-8,30,17,-23,20,-72,55,49,-24,-1,-17,7,-42,23,59,42,-27,87,-83,-47,99,68,-46,91,18,-93,-88,28,20,40,-12,-88,-30,-95,-12,66,-90,-79,16,-38,19,75,68,76,-2,27,-5,71,-9,12,-99,-32,-43,-46,-41,74,-40,-53,-21,79,86,67,68,-66,48,-67,99,57,-47,15,-81,71,-33,86,25,65,-10,96,36,58,-15,13,-74,41,66,-39,-7,-97,7,71,59,-6,15,27,4,-36,59,3,-79,89,95,-83,37,-38,79,-38,-96,-53,-41,39,-95,43,-71,-93,-38,71,-33,54,74,50,2,10,-79,-82,-86,24,-19,49,-95,1,38,99,-6,-24,-62,-26,14,-58,20,49,57,1,-7,63,-16,31,34,50,-15,-15,-23,86,94,-2,-96,-92,98,-39,34,-97,62,-28,78,-67,24,93,6,-61,-65,-97,87,68,-20,-43,31,63,87,-57,-10,-51,27,67,-87,-1,-35,-84,-17,-60,-23,-83,-57,-84,-34,-79,-52,89,-86,31,-95,-75,10,69,70,90,-97,1,53,67,43,-56,-84,-52,87,-72,46,-71,-79,-71,-32,-26,-77,10,-34,-12,8,-10,-46,-2,-79,-41,0,8,-95,-30,-2,83,47,-72,50,-9,-29,43,15,-65,70,-39,-37,67,-34,31,-59,-12,-82,6,75,25,96,-70,-99,93,-35,0,1,-54,69,75,-71,16,-96,56,83,-49,-1,-2,-14,-31,35,48,-86,-98,-21,-46,-34,-3,37,-58,98,10,-52,98,3,-11,-2,81,11,-33,56,16,60,36,-28,43,87,47,-81,-50,93,53,97,-93,31,-46,-40,97,27,73,-84,25,-17,-60,1,63,5,98,44,-84,-57,-23,8,79,90,57,22,54,4,17,-96,-3,-29,-99,3,78,-69,40,52,57,13,67,-40,73,83,60,36,-12,35,-43,-20,54,10,88,33,0,45,-67,-46,-51,49,-43,23,96,-65,-74,52,-35,42,4,99,-67,-28,-41,-94,-45,-81,18,43,53,74,99,-15,-39,87,-82,61,9,-73,91,58,76,-74,-19,49,-63,-17,1,1,-97,-94,-23,-65,-46,35,-83,8,53,34,-72,-16,-15,-95,68,45,91,62,-17,1,89,-48,-64,42,-46,-7,-9,-10,52,69,67,54,74,-55,65,-72,79,58,12,10,-31,17,70,53,21,38,-24,-11,-23,35,89,-34,86,-98,-92,-60,-6,-24,6,-53,-55,-26,77,-81,18,20,-77,-26,-22,11,60,47,-72,30,-23,25,-55,52,-85,22,-12,80,87,-49,59,72,-32,-47,-52,73,-24,-8,-76,-69,-13,18,50,9,92,-95,96,52,51,-98,-40,-71,26,4,57,17,-74,-78,-25,90,-50,-66,39,17,-37,86,-33,39,-45,-9,69,41,-91,-4,-73,77,0,-77,7,-48,-76,66,-43,50,-30,90,-56,-27,-87,-5,-37,-38,28,-98,55,91,64,-78,7,-81,12,-47,36,-2,48,62,-25,-75,84,81,-47,-91,24,-14,35,94,-23,78,-56,-34,-49,-17,27,78,-16,-18,46,-75,-20,-70,-80,92,-18,55,-10,-93,17,41,-68,1,0,-39,-14,-76,47,-79,94,-76,76,-62,-11,-73,20,92,81,80,-49,28,-95,30,34,-99,22,-83,55,88,99,-28,7,-69,50,-93,-8,-64,-93,-61,-66,-98,-61,86,-61,27,-87,59,-4,70,16,46,-25,-2,-24,-90,-2,75,-74,-46,40,-98,2,-53,-67,-48,-70,1,-35,-63,16,-2,-62,31,-39,-47,-65,-27,88,30,-80,5,-24,-5,-97,51,4,0,26,6,30,-33,7,-67,-10,16,-39,20,93,25,56,-14,99,70,-83,-40,-77,-49,9,-88,80,29,16,-67,-99,-5,84,-19,71,-13,86,2,30,-30,11,-79,63,71,17,33,-26,-27,-80,-27,-57,-87,10,-35,-36,95,-47,-79,1,45,-69,1,-60,-85,81,-88,-22,44,-10,85,91,-99,-94,31,48,-1,-36,-78,71,-40,-28,90,-27,58,-68,13,53,-15,10,-45,-70,40,32,-30,31,-9,-42,86,-65,24,71,-97,24,53,33,-51,-48,97,-29,99,-66,42,89,6,0,-79,95,-70,5,6,-39,12,-54,93,58,54,-16,92,40,-5,16,11,-25,-83,-59,-92,-35,-8,81,35,-9,-84,-46,-43,-2,30,-23,-6,60,59,99,97,-29,-78,90,-94,52,-49,97,-8,23,13,79,97,6,-80,-95,70,-12,63,-17,55,55,36,-88,-47,-56,-34,23,-96,-98,22,-99,-28,21,68,-46,-50,95,-49,42,18,40,-2,15,-54,-5,-3,-84,82,-63,-25,15,91,-88,3,-56,-68,68,67,-88,69,-34,88,-82,63,56,-29,-86,52,-2,32,-53,-62,-70,62,-17,1,-64,-24,-39,-28,50,75,-37,38,-22,-17,69,-53,-73,80,92,-30,69,-89,-67,2,-42,-77,-69,56,31,-22,93,61,-83,-46,-61,-48,6,-1,23,-67,-26,62,48,29,-55,17,52,-51,-25,44,18,-79,31,27,22,89,50,53,22,-42,-92,-8,-81,-76,22,-65,-25,-72,33,74,-62,84,13,85,13,57,2,-58,82,53,62,0,73,-6,-72,-27,-40,54,-74,58,-88,-90,-50,-92,-67,72,-81,-16,76,51,-65,-86,35,47,98,-75,-19,-22,-57,-36,-69,-94,40,-95,-24,67,-46,35,-2,-44,-7,-13,-35,19,-29,-3,-9,-11,57,-55,-83,91,-42,29,38,-43,53,95,34,73,-41,41,78,99,22,-46,43,75,65,-81,-69,-65,-18,-5,53,29,68,-78,-82,25,-34,-89,-7,23,39,-69,56,-30,-96,-33,-57,-38,-91,97,-39,30,-49,81,6,92,99,36,-73,-42,-68,56,86,76,54,80,2,96,90,94,20,7,-97,-47,76,-94,20,-81,-56,28,-84,-18,-42,-57,-37,40,-88,-61,-23,-62,-4,-15,70,-18,-39,2,-61,39,-2,-71,34,94,35,13,-52,-12,18,67,-17,38,-28,-25,-80,6,17,-18,-53,5,-3,0,42,92,61,-10,-49,-78,91,-11,61,-11,-5,-28,-16,-93,84,8,-5,-21,-48,54,-83,0,-70,-86,-94,23,-5,-71,-71,92,5,47,61,-34,-63,89,-35,-95,-22,-74,-29,49,-26,31,33,-42,-61,-95,13,-10,58,6,89,87,19,71,-12,91,77,16,60,-18,-37,21,25,-23,10,89,-42,65,91,28,-9,-35,-41,-76,-1,-26,-72,88,40,63,-6,6,50,90,-45,-62,81,-68,30,41,-10,93,-61,-85,-53,26,80,4,-9,71,-90,58,-64,-55,82,11,19,86,-1,-64,49,70,42,-23,60,96,-9,18,-72,-78,-41,-6,91,-26,9,-62,99,-11,41,-33,-62,50,-74,-27,95,84,61,-9,70,-40,26,-3,-93,-55,73,66,-59,-59,-16,-55,-38,19,39,-47,93,-52,-10,69,13,-91,-63,50,35,-38,-99,7,-54,61,74,92,97,-22,-11,-95,22,-61,47,63,-20,-91,-92,18,27,23,71,-3,47,-62,-33,-39,-77,-20,87,35,41,87,-81,63,25,93,32,23,-29,98,4,92,-63,-72,32,-7,-64,17,-88,40,-60,59,-86,87,73,-43,-75,73,36,-88,8,-46,99,3,-83,1,-4,26,-99,43,24,-19,13,60,9,-55,-69,44,61,-81,-39,78,54,-25,65,4,31,89,-23,-55,77,61,-2,53,-35,-8,-45,37,-82,-45,-19,41,36,93,-22,-78,-85,8,65,76,3,-96,54,-43,-45,-4,61,62,-38,-62,-93,-61,76,-18,69,-82,73,-76,54,67,-45,-88,8,67,81,62,88,96,-52,54,49,50,34,-20,84,88,52,45,50,-86,59,57,-71,35,-84,97,29,88,97,-16,55,-47,-28,-60,-80,-46,78,-91,-73,-74,39,52,53,-50,-68,37,-62,60,-18,64,73,-82,-2,78,30,13,53,-41,-22,50,19,-90,79,91,-51,76,-78,-95,61,-75,-70,-23,76,59,26,84,-4,40,44,54,-19,-6,72,79,-51,2,-8,-98,37,47,29,-43,56,-15,-75,-94,-39,-77,86,98,-53,-84,-25,99,75,77,60,-52,-6,-19,-97,75,74,74,54,-77,-47,-77,-98,66,69,30,-77,26,-85,-76,8,-47,-54,-6,-49,-31,-14,3,-55,-62,-20,-95,-14,51,-15,-35,26,-64,-84,-43,-41,-32,-44,-63,-89,-97,66,-89,28,57,-66,-87,-90,-43,-17,-39,2,45,40,47,83,96,51,-54,47,-86,10,-50,-51,2,6,-16,46,62,20,56,64,-14,66,-31,-56,77,-42,-70,-66,17,-33,12,-38,-93,-41,-78,-96,87,-56,27,-99,30,77,-51,-68,-40,33,77,98,-70,34,39,16,0,-92,36,-23,-58,65,-13,35,-67,99,97,-84,-65,95,-81,-78,-60,23,98,69,0,-52,-98,59,57,78,58,86,-11,-3,-21,89,-18,91,-57,0,57,7,-64,66,-17,-90,81,17,-95,77,16,-79,0,14,90,99,38,68,35,-28,23,-30,-64,-87,67,14,-98,-74,6,-79,25,-60,4,37,82,86,46,63,-19,28,40,96,48,-60,-13,15,-84,-74,-17,28,-3,-93,97,9,95,41,-99,96,66,6,93,-31,22,-2,82,4,-16,29,-56,41,-66,84,37,58,-99,-75,-26,93,-73,33,21,0,16,18,-90,11,-63,-90,-16,-97,-8,-45,-52,-86,52,-69,-6,-87,36,37,54,69,-2,-32,27,-1,-8,77,-31,-5,-12,66,95,80,-39,-95,-31,-3,90,52,0,-18,-93,47,-28,35,54,65,25,-10,-21,-21,-41,77,46,63,-47,-84,17,-2,10,-95,-36,5,85,24,-14,-46,-78,-24,82,-2,34,66,-78,-94,-22,76,47,-97,-34,-96,-42,2,57,81,-58,-90,96,58,7,-17,40,47,65,2,-29,-72,55,-31,-19,14,66,-85,-43,65,97,35,41,21,14,83,24,72,-38,-19,53,3,-33,26,-61,73,85,78,-3,50,-20,68,78,-88,-63,-41,2,80,-50,59,45,-53,-6,-37,68,84,-77,-31,56,-38,27,-14,64,93,88,79,44,74,57,-59,24,-86,-91,-21,-75,-77,14,4,79,41,-37,24,87,33,63,32,17,62,78,-49,-76,5,36,65,-2,25,44,-58,-24,-21,-40,76,-8,-32,-44,-6,-33,46,97,-54,-13,-63,46,-48,69,9,60,-37,-28,38,13,-5,-57,-73,-63,18,28,81,59,-96,-40,-81,79,28,-36,-88,98,7,58,72,53,-78,-91,-1,-27,54,85,-66,-82,-66,48,7,5,91,33,42,9,-62,0,-55,-59,36,-59,-79,-36,-19,-68,-60,87,66,-88,17,88,97,93,-62,51,55,-52,45,88,96,-47,-7,64,62,-88,-50,-99,11,-6,-82,-53,11,-62,-12,68,-53,27,33,-87,38,-50,77,12,-80,92,-36,74,-60,-91,39,-87,-62,-90,76,77,-79,-74,54,9,-3,71,55,84,86,-57,53,-67,46,-14,-78,-38,12,76,73,9,68,-86,-40,-92,-77,99,97,-63,85,73,-86,-94,76,44,-9,-50,16,-53,-89,2,-34,63,34,89,-74,32,-49,15,8,-76,-99,-24,-62,-40,-39,-63,-41,-42,-50,-56,-92,-59,-73,60,84,17,-90,0,40,97,78,83,37,-11,72,40,-78,-77,-45,29,-77,-45,82,-63,-9,-80,-50,50,-46,0,70,-39,17,73,98,1,-32,-92,78,84,81,56,67,19,-54,39,-41,-33,38,13,72,38,44,31,51,-65,50,-98,61,-96,-22,9,-58,94,-41,-60,-5,26,-76,-27,11,-94,-70,-45,24,-48,71,82,18,-14,-28,-33,-76,92,98,75,-96,48,53,42,29,-69,-49,47,-75,-14,86,-4,-87,86,69,0,68,75,54,-8,-73,2,-49,21,88,-1,87,-88,-9,62,63,-5,-12,16,-63,-83,46,-36,40,47,49,26,-56,38,-11,89,-85,-42,41,46,26,44,-52,77,-58,-64,-24,-94,-52,44,68,87,-61,-44,4,-48,-51,-73,-8,65,51,-82,-9,71,56,56,60,70,-86,-22,-7,40,-78,41,-6,-60,76,46,-55,-99,-10,-87,65,5,-55,-31,33,-30,-28,-75,-65,99,-57,2,70,75,-64,7,22,-51,84,-84,65,82,56,-64,-78,9,82,-33,10,-28,-44,-25,54,-22,20,-13,24,68,12,36,68,31,-62,38,6,-27,-54,-72,-1,-93,-57,-59,89,75,-23,87,-15,-64,-69,71,7,-36,-77,-62,18,19,25,-58,-13,-63,77,-68,44,92,47,-50,-58,69,-23,17,75,-3,58,41,-28,-88,6,33,-53,36,4,30,99,3,68,-6,-78,-7,36,-14,6,-10,17,-50,-18,-36,-24,24,-67,29,-59,85,-74,75,26,-25,86,-68,-92,-67,45,-11,63,21,91,8,-84,90,77,51,-24,-17,-59,92,9,0,-66,84,-99,-34,-10,-82,-72,16,93,31,67,56,39,51,89,-16,-60,29,-94,-91,-86,97,98,90,25,-26,-50,42,-57,58,-58,-24,19,-58,19,-91,-63,46,1,-70,-23,-32,85,-83,-80,51,0,-64,-43,-18,-56,-30,-21,-58,-40,80,-8,9,23,35,-56,64,-89,39,83,29,48,-80,-24,-51,-74,29,-6,87,45,13,39,-77,48,72,4,69,-80,60,87,-21,40,-20,65,-60,-85,85,81,-98,25,64,31,-50,60,83,-2,62,12,68,49,-42,-19,-35,-20,-93,-85,60,75,-66,-3,62,-11,-85,-81,-69,-46,-67,-83,-65,-65,41,75,42,67,12,25,-35,-26,-63,-66,-99,-29,-9,-58,27,-26,-44,-12,-74,-11,61,65,78,75,83,-91,-93,93,-98,-59,-95,19,93,46,-14,5,-52,28,56,-39,38,56,32,-94,97,-41,-20,-69,23,5,19,-38,-30,-26,-63,-69,-40,-57,-76,-62,-39,-72,57,-46,50,-57,58,97,47,-9,-42,-15,-53,66,-9,-78,-97,70,-48,2,-48,47,63,-1,-78,-99,29,-42,-80,52,-5,-20,56,-48,10,6,-28,-31,-20,95,59,37,-19,83,-19,71,-95,-17,18,-67,61,46,79,25,-55,77,2,50,-88,21,2,7,78,-65,35,-12,40,83,33,-80,79,-30,34,-63,-47,-85,84,-66,-26,2,-34,-65,-75,-78,36,-30,76,-62,-80,87,59,-1,-29,37,33,83,-75,-49,66,58,-53,22,-72,57,58,-43,48,42,-10,-78,-79,32,-66,-54,30,69,-8,6,-92,-12,-29,43,63,41,-43,-3,24,-19,24,-32,-84,70,89,-80,5,48,-24,-47,-33,42,-25,-12,-49,-15,10,81,-69,-98,-36,-85,-11,34,57,-47,-47,-86,26,76,-28,-73,-79,-36,73,-89,-16,-22,35,36,31,78,-44,82,-34,6,-33,75,-36,-26,53,5,-11,-80,-84,-77,-28,-32,-63,74,-78,-15,-99,-58,48,73,-71,-91,-48,40,22,59,19,77,41,61,-40,84,14,1,-42,-33,-94,46,-37,-79,69,34,-34,82,-15,-13,-56,-15,5,68,-64,11,77,-36,-49,-24,-77,46,-47,63,8,-11,47,98,89,-95,-58,71,28,5,69,-3,-61,-65,-44,1,-2,-1,85,-97,-56,97,-10,-79,-39,41,-4,-17,-13,25,-54,71,91,92,69,57,97,88,29,2,-7,-2,98,8,9,-69,-91,83,6,71,62,49,68,-47,47,-70,93,-80,12,-43,22,58,-94,13,50,51,-30,24,39,75,-74,-68,-50,-99,17,35,-92,25,18,-10,-4,-19,-60,-35,33,63,-6,3,82,82,59,4,40,41,93,-32,-7,-59,68,-91,-84,71,-82,-57,48,34,77,56,-64,-4,-77,32,76,-38,73,9,-75,-56,-88,84,-74,47,-12,66,-34,-41,-89,35,-1,78,43,-9,49,37,33,-25,-29,11,-92,7,83,-70,-84,59,-8,88,-55,-7,-91,-67,-23,-66,79,42,76,-78,77,86,56,-24,65,-23,43,-9,-86,-23,65,-38,64,49,68,47,79,60,6,-29,25,27,40,33,59,-82,66,15,36,20,37,13,6,-30,65,-52,46,8,16,60,61,-42,-78,25,-92,66,-51,86,26,54,-66,-49,-19,73,60,-83,67,3,32,3,-77,-31,92,29,38,34,76,-38,-57,-31,-78,80,27,-80,6,34,85,54,20,-12,-14,53,15,43,26,-25,60,-29,54,-31,50,77,37,43,6,-48,-46,-41,13,-4,28,11,-46,-68,30,36,65,-8,-10,-15,56,52,-85,-52,-27,17,-1,-67,87,-46,-22,38,-69,-85,-19,13,-57,34,48,33,-92,-47,-56,-62,-16,51,73,-51,-80,-60,10,53,92,24,-99,-35,-58,0,-26,-71,30,51,66,60,42,-76,-50,61,35,97,-6,19,-49,15,56,34,-57,6,60,-38,45,-30,91,37,71,92,78,-87,-31,-71,-82,98,79,61,35,-2,61,84,-63,-27,81,30,68,-91,-78,24,43,-36,-93,3,3,52,49,-6,-11,20,-37,-55,9,31,-27,4,6,-70,-35,-59,27,-97,-75,40,-24,-93,-29,-56,91,-31,45,34,10,51,-86,89,3,63,-17,69,-40,23,-86,69,-46,-14,-27,60,-8,14,-99,96,16,-97,36,68,85,-93,-87,76,-47,34,11,62,-38,1,51,65,-59,-89,11,1,33,24,-53,64,86,-4,1,-44,86,-22,-48,-21,-20,87,-52,-35,71,-63,-58,-76,47,29,62,-91,-93,13,73,-52,0,-39,25,-66,61,48,74,48,-79,-25,-96,-93,52,-68,-38,-67,-81,-14,-26,89,22,-8,-87,-31,-79,74,-45,-95,-36,-72,-71,64,-34,53,74,-73,-22,25,51,-25,99,31,-19,28,62,19,37,81,-94,-88,70,4,3,83,50,1,34,-95,-18,75,-91,10,39,-26,-60,-10,1,17,-85,-48,91,90,83,-51,18,45,44,-44,3,49,-56,-26,-46,46,-66,-96,-76,67,-92,5,42,-84,-85,-42,-10,-46,24,67,47,38,-81,15,28,78,40,-76,1,-15,-21,-96,-66,22,-23,-36,-55,10,-33,-54,-45,-49,50,73,-33,42,-91,33,95,32,-23,20,-52,-5,-65,52,-49,52,75,51,-63,-69,54,-30,29,-91,34,51,-5,77,96,26,-71,46,-23,-28,-12,-15,81,-39,93,-42,57,-82,29,68,47,79,20,-1,7,56,30,-61,-96,-64,-53,14,86,18,-9,82,-55,-4,29,21,44,93,82,2,-69,52,36,87,70,-34,56,17,-78,-24,92,6,-67,22,44,-87,35,90,26,21,-15,93,4,29,-10,-90,-73,-89,79,85,13,-89,38,-51,74,-15,-9,30,78,-10,83,70,95,92,-30,39,-95,-95,6,30,2,90,0,-94,-3,66,91,23,77,48,-14,-33,35,-76,-8,9,-15,83,-83,-37,-27,76,-90,-32,68,-21,-93,49,-40,-11,-44,62,-21,55,44,52,22,13,-24,-24,-39,61,42,72,61,-66,-42,-54,-83,-26,-15,-34,-73,-29,10,94,27,-7,20,86,81,75,48,-62,8,-30,89,-70,82,-58,5,-80,-97,-76,91,40,-43,-51,62,-49,0,-53,16,26,-5,-73,-2,-78,19,-82,-92,-22,70,33,15,-22,-97,4,-16,61,46,65,80,25,88,48,-34,-55,96,-95,-5,-27,-71,88,99,23,91,-26,44,10,-32,28,64,-62,-39,-21,-8,-60,83,75,77,6,40,57,-69,28,-18,-27,50,-21,-22,-78,28,6,-90,4,-71,-99,77,49,-12,-54,-23,-48,-40,15,8,29,31,-32,-19,9,73,-78,-57,80,26,25,-46,-24,80,8,-25,8,90,-16,-87,95,-38,66,44,26,88,-79,54,-51,12,-38,54,-56,29,-65,52,-21,-44,71,-40,59,-4,-10,-88,-47,97,-14,61,87,47,50,82,85,16,3,-12,5,0,-58,30,-87,-19,-16,-44,86,18,84,-34,51,32,2,-13,-71,91,-2,-19,65,61,-81,52,8,45,11,-30,-38,90,57,43,-10,98,-50,2,-44,33,34,-57,-72,-5,-15,55,-72,86,-58,-67,77,17,-10,42,-45,-14,-29,39,-69,58,-91,-31,48,65,-88,-85,40,-39,-6,96,70,-95,-84,75,0,0,7,4,-37,26,13,-60,-57,-97,58,-3,-12,-94,-64,-4,40,-79,64,-35,85,53,-21,2,90,72,-25,38,77,-10,13,-46,66,96,34,-94,22,-53,-55,41,-51,79,-85,14,61,-73,-90,1,-53,50,65,-91,3,-78,11,-6,70,85,-68,47,-47,21,77,95,17,11,-98,-83,57,-77,57,83,79,72,-26,40,98,-40,-81,-54,-90,60,-46,13,58,41,83,29,4,91,-47,56,12,-69,28,-94,18,6,-78,-24,29,56,-64,-15,28,9,-98,3,45,-80,25,54,57,79,-56,15,-3,-73,-56,-99,-82,-3,33,6,27,-38,12,-78,44,10,-26,-27,-34,9,34,93,94,36,-26,39,55,98,-29,12,54,14,-95,-48,41,-52,-48,35,21,62,-58,-75,-99,30,-53,44,-83,20,94,-17,-70,28,-47,-99,-36,26,17,96,25,87,-15,-21,1,-11,7,-81,37,59,54,-42,-2,72,-17,-2,-21,6,-58,-5,-74,-64,77,-68,64,-92,-67,-72,33,49,-76,-65,36,-14,-9,-86,74,97,-67,-12,33,63,23,-69,12,-94,28,90,11,70,-38,13,82,-60,45,46,-76,77,51,56,3,51,68,-61,-63,-64,-48,-88,-67,-39,-24,43,-76,98,73,35,80,-21,2,-32,-74,64,81,-92,80,26,54,-96,-20,-18,36,82,-67,-19,-79,-53,16,-51,-65,49,-13,10,-8,-13,9,-58,99,-11,20,1,57,45,-35,15,30,-78,-59,-39,-75,20,42,38,2,51,-81,-1,97,35,24,-91,-39,87,19,29,-25,-95,70,-26,-30,-32,74,-96,89,-83,18,19,-62,58,79,-60,-45,-2,77,33,-50,72,-68,-76,7,33,-67,44,20,51,-27,94,32,-56,-55,-98,-12,-80,-94,-23,-87,23,73,-73,-41,29,-34,13,-72,-80,-76,-23,69,-45,0,-47,64,32,97,-38,-40,-30,-44,91,-10,1,93,54,-3,75,-91,-14,-2,81,12,33,10,55,-76,37,51,-53,90,20,-22,-32,73,-57,99,47,4,-63,93,36,-95,-16,-86,97,-62,-13,49,-54,72,-75,-96,-15,57,-9,-83,80,-72,67,-73,95,-35,-18,-37,-85,1,-61,61,81,-25,54,-6,-20,-85,8,-46,-70,71,-96,-48,21,-72,-44,82,61,46,98,42,50,42,45,45,-93,-73,84,97,4,-76,58,-15,-2,-10,79,54,-19,-36,-91,10,-65,88,62,55,-84,94,37,53,40,12,-5,-33,-45,-82,-87,-62,-79,96,-64,25,96,70,-90,-5,-40,65,-74,18,-71,-66,-72,-59,98,66,72,90,60,-13,44,-23,98,-61,44,-70,-67,33,-32,-46,6,3,55,3,-27,64,74,10,7,76,-72,35,-89,-68,52,85,98,25,76,35,-88,20,89,-90,58,10,-83,68,-57,-16,-78,25,86,76,-95,-41,17,55,45,-76,32,72,36,19,-95,-12,4,79,-87,-20,14,-99,99,-20,87,35,89,-96,3,-91,-13,1,34,-50,-46,15,-15,70,-29,-69,71,79,-97,-16,-2,83,71,78,62,61,-41,-46,61,-65,33,48,69,0,28,-51,8,-85,26,-81,-36,79,34,49,27,81,56,-25,60,58,58,-42,19,29,-87,-19,-33,-29,11,-71,6,-78,53,-48,21,-18,-22,-71,-27,-96,-75,14,60,58,-60,-13,39,95,38,-24,30,-4,33,-51,-98,22,7,-31,93,-82,-26,-24,-61,-96,4,36,-38,58,42,35,39,66,-51,-1,24,-35,62,-60,-40,0,15,89,95,-75,-61,73,46,45,-58,16,39,15,91,78,19,-27,-9,80,-69,-67,-8,69,98,17,-32,-1,81,-93,15,-59,-17,-70,-92,-45,-69,-77,-71,54,67,-30,-30,6,62,-61,-39,-42,11,52,-85,41,61,7,11,60,-99,55,-64,82,39,51,99,-78,57,83,-23,88,-94,-18,42,72,51,88,-44,-10,-73,-7,47,37,-78,62,-44,83,-54,43,20,-54,-25,55,-95,-86,-17,81,-87,-59,64,-34,-94,70,47,47,19,-25,35,51,65,39,-78,12,-24,-80,-49,8,79,-27,-49,-1,-4,26,-68,-23,16,-9,-42,28,31,99,70,36,69,17,-40,-35,92,72,93,57,11,-85,-54,63,-89,-26,-28,90,46,-1,-11,-58,-98,-3,19,18,88,53,-77,-4,52,93,-67,-2,10,-31,40,-21,-59,33,-64,28,24,-41,-8,34,32,40,24,-22,-84,90,-3,-82,-36,92,12,-48,45,11,25,-25,4,57,49,91,-74,-11,-53,-56,98,-17,71,-1,41,-60,-89,-27,56,11,27,72,1,-76,66,42,92,-22,70,38,88,-5,89,-30,-71,38,-62,-68,-95,-16,-25,79,43,-77,-21,-16,-37,-34,33,-81,76,-62,67,-45,-62,33,96,-69,87,66,45,76,-61,11,-77,-33,-51,-40,-2,-70,20,72,86,-36,72,-35,24,-65,30,-42,-70,-17,-28,74,37,9,7,10,16,-5,-23,-39,-52,-8,71,-53,58,97,-17,-43,-96,-97,-94,89,-34,77,-69,90,88,37,-75,-81,-79,-4,69,34,81,-24,-55,-2,47,-2,35,71,89,-16,94,47,-19,-23,-96,-39,-20,86,-49,45,63,-42,35,29,95,36,24,92,-68,-7,26,90,45,70,-12,-30,-32,99,-59,-43,-17,-87,81,40,-11,84,-98,68,47,-71,-9,-12,-14,-97,-83,-42,39,40,-50,47,-67,53,37,77,23,-98,-53,68,-98,-35,-75,-39,-23,-94,-98,65,67,79,11,-9,84,78,78,-53,80,94,-18,-4,34,31,-56,66,-16,80,21,84,59,67,52,37,-68,53,97,-15,36,75,-72,-20,31,38,70,15,16,49,39,-27,20,-79,69,-45,51,-87,97,-87,69,18,96,28,-37,25,-35,-29,-22,-60,56,-86,-85,60,-30,46,-2,-59,-62,90,66,76,-37,-14,96,-68,17,25,-79,15,14,90,-90,-13,-5,-51,-88,37,-3,-34,53,-47,-43,67,89,26,-10,-13,66,28,-23,9,-19,16,95,-22,25,12,79,45,-96,-7,12,90,79,84,-61,67,-2,35,-67,-49,64,-11,94,53,-84,-38,-83,58,89,-30,-32,-53,86,-60,1,-12,51,-20,-90,32,49,22,22,28,-17,37,-5,57,-50,5,-92,-86,93,78,44,-91,-60,37,67,-94,-92,-88,-47,70,-49,53,-42,78,-89,-33,10,59,65,-91,-35,-75,46,36,81,95,-59,65,85,-65,44,6,-80,83,-56,63,89,-72,74,-81,97,-75,48,-68,80,58,-25,-10,-5,-59,-1,36,-58,-78,-28,-76,93,-10,65,55,1,9,-38,20,-30,-18,-39,-64,9,-65,-46,-17,-63,-98,14,-83,37,88,-17,-91,-94,58,44,-52,79,92,-52,49,-18,-87,5,82,-1,43,-20,68,-98,40,-96,-13,74,-66,69,87,-88,-40,80,25,-52,-36,33,-69,-78,-23,-22,78,-30,2,27,51,14,-91,11,89,28,90,57,29,7,37,-84,-19,47,61,-54,36,-79,-74,-39,-54,-34,94,-24,-35,-29,30,-57,17,-68,46,-54,22,32,56,12,-40,23,-54,66,-70,60,58,-13,-16,20,9,-80,17,35,-19,62,77,-25,-85,-58,22,21,-16,-83,52,-92,-38,-48,39,94,40,98,17,62,41,23,-1,0,86,83,-80,-4,-97,13,-92,-17,-47,84,34,-33,-73,-66,88,-13,-73,17,-6,-12,45,-90,-41,-15,85,52,-75,26,-25,23,-74,-39,6,-78,33,9,35,40,68,64,2,-20,-69,28,-10,95,91,16,-10,-37,-96,-65,-28,-38,-3,-66,-86,21,60,-35,-56,62,2,50,84,-64,-64,-4,52,80,-40,-46,-40,-33,58,49,-60,50,-35,29,-87,-55,63,-39,-17,-40,-28,-27,57,-68,14,-98,93,-83,28,54,-71,63,-73,57,20,-37,-88,80,7,69,6,46,-4,48,-25,-15,92,-85,46,-47,-25,-82,2,-91,-74,-83,-90,95,-90,37,27,-85,-23,53,71,97,93,82,54,0,52,-40,-54,-52,-92,20,33,77,11,-44,-93,62,-50,8,71,-48,1,80,-53,10,-5,73,24,48,4,-4,22,-3,-22,-24,96,-93,13,-81,-68,-3,15,41,-49,-74,73,-43,88,99,42,59,-49,-57,16,-26,53,87,-52,-46,36,28,49,-65,-98,-95,-12,74,87,-99,92,95,-26,7,13,25,9,-14,58,-3,-15,0,-67,12,20,26,86,-27,13,-89,3,-74,38,-70,-39,39,-66,48,-10,97,25,-18,93,98,65,6,0,-49,69,-41,25,-69,35,57,43,-45,-40,6,4,73,16,-92,98,-46,-63,-64,69,-53,60,-64,-56,-15,-6,-86,-39,-64,-3,60,-14,-34,-81,-89,-27,54,45,-84,85,-95,21,-10,54,-86,-3,30,-56,10,65,89,56,26,-75,99,87,18,-86,-52,53,10,-91,-60,52,-96,-73,-75,34,71,-82,20,53,15,-90,7,29,-17,-63,72,92,-97,62,48,5,86,24,-8,-18,37,40,-65,-76,48,-26,52,28,-22,77,-37,-51,71,82,-98,-14,68,9,-85,-49,22,64,-57,24,3,67,-94,-11,-9,-2,70,-94,-62,82,-94,62,-44,58,-33,10,12,29,59,-17,11,37,45,-44,-54,37,6,45,1,25,-31,-96,-8,-25,-31,83,49,-83,88,63,98,93,2,-69,28,68,41,-60,-2,0,-1,85,-63,-55,-58,-40,81,47,-95,-41,-50,-50,-38,41,1,7,24,-50,23,-11,-87,21,-40,14,52,87,-40,-7,-72,57,69,3,42,82,47,60,-81,5,-15,99,63,34,-73,-98,-25,27,9,76,54,-68,-35,43,30,1,-65,-41,-11,-6,28,-7,-72,-26,95,69,-44,20,7,-48,-75,91,-72,88,25,-46,66,76,58,-25,29,12,-16,71,-68,90,-28,-57,-51,60,36,76,-70,63,-73,-74,10,-18,22,-83,10,46,84,38,11,-14,91,-22,-38,49,29,68,-62,89,39,-53,79,-89,-11,-95,48,-97,57,77,42,83,79,-48,-34,1,-55,52,-52,-94,-10,35,-9,-41,-87,30,84,42,-2,99,31,-63,-54,-12,-76,11,-8,71,13,-50,26,-44,-67,5,-16,-25,-93,29,-72,-69,34,17,65,-97,75,55,32,60,-26,-70,59,81,-57,81,-31,-34,-8,61,-85,82,87,40,-62,-80,-55,21,-28,-72,-73,-1,-65,38,92,-99,40,45,55,-51,-18,-94,-45,-82,86,-3,98,-44,39,-33,93,53,-51,57,-7,-37,53,15,61,-75,42,64,0,77,2,-7,54,-81,-85,-14,-56,-4,-9,-2,-10,-23,71,-12,9,11,31,-21,-59,57,-64,11,-80,89,-74,80,-86,44,22,-9,-2,-76,83,-48,-80,74,14,-37,-30,-95,38,59,-41,9,-76,44,96,31,-76,-85,-12,-64,25,-15,-75,50,-58,-84,-6,63,6,92,64,-34,-79,83,-60,35,-77,9,16,37,-55,51,-76,-55,-27,96,75,-27,-89,-59,8,35,25,33,-38,66,25,33,30,-69,2,-6,-27,22,-46,12,-66,-47,97,27,90,-81,-45,-86,-37,27,-90,-62,99,97,-22,-15,32,-97,-82,71,46,19,4,-47,26,-94,46,98,4,76,10,38,-71,-16,-58,95,2,-4,-91,64,-99,95,78,76,92,-66,-39,1,-87,-45,-28,58,73,75,-89,-1,57,33,-26,-38,9,83,76,15,-56,-82,10,45,-10,-4,9,-33,-9,-35,-56,-40,-2,4,37,10,59,-90,-31,9,61,-21,-91,19,89,-18,80,-2,-57,56,89,-14,50,0,-91,-83,95,-6,-16,-37,58,27,-1,-44,-92,-64,66,43,-55,-88,-47,-93,-33,-39,2,-44,19,-18,31,38,-85,20,-98,41,-80,-90,57,91,3,-82,-46,-38,21,29,-6,29,65,-63,-28,-90,-52,24,92,15,61,-6,47,-42,52,-22,95,43,98,96,-39,94,82,-81,86,-14,-87,-83,24,11,46,-82,-60,-12,-45,-12,-26,-21,89,-33,93,27,37,41,84,-33,95,57,86,70,30,-52,65,13,-57,28,98,-45,44,-1,65,-33,-7,81,54,24,-53,-71,-96,-64,-28,73,39,85,-9,24,-71,-13,-42,-84,-43,87,-37,98,0,5,26,-25,59,-52,50,2,-9,-56,-40,-54,67,6,-49,47,18,22,21,-42,-16,88,58,13,-48,-84,28,9,79,90,-16,-20,-28,-89,31,-92,-42,-18,9,25,25,69,70,-31,-48,97,93,70,-4,-9,-95,80,-21,39,-30,31,31,97,-83,10,64,0,89,-64,-13,21,-57,21,79,29,-53,4,-25,93,49,26,91,42,-27,-13,-67,-46,-56,12,92,13,-80,23,-13,-64,-66,-49,12,99,-14,99,-3,6,-3,-24,-65,43,79,9,37,29,-65,5,-52,-15,91,-19,38,-87,69,31,25,88,-69,-87,-99,-36,-37,-11,-36,26,-35,60,-68,62,-63,-57,5,92,51,-81,-2,62,23,46,-53,-8,-96,85,4,72,-7,-71,37,23,-82,14,64,-42,-97,-95,60,-55,64,68,-93,77,-89,-12,47,61,-16,-78,23,-93,67,47,-25,47,9,78,-4,78,84,-90,-22,78,23,-58,-64,3,-54,95,47,87,63,30,41,50,94,-12,11,-22,10,-88,-38,-46,35,13,78,-56,-8,-26,98,-47,-16,-24,-69,83,18,-56,-37,40,-61,-90,27,79,16,-54,6,-12,33,94,65,-80,82,-96,-49,17,17,-71,37,85,-21,35,-62,39,87,-55,0,5,-12,62,-77,4,72,49,-40,-35,71,65,52,-18,59,-5,1,41,-2,28,-65,91,33,71,53,89,-17,90,28,-29,-87,-72,75,0,90,74,-96,39,24,-60,80,-28,-94,33,53,41,-95,-68,-17,-21,59,17,-29,-30,-34,-76,-41,48,91,63,-81,-96,68,71,-20,35,45,-39,-26,-54,0,-69,18,-18,40,-29,-76,44,2,-17,-76,-61,99,-29,8,-58,-29,43,90,-38,6,85,-58,-49,56,22,85,-21,59,-64,24,-41,-33,-81,41,-93,-33,64,28,45,-76,51,83,-77,-78,-32,-58,-8,87,-68,31,-29,-83,49,21,50,-52,7,-71,-93,19,29,-34,85,25,83,69,91,47,-3,36,47,-75,-3,69,-54,41,87,14,6,-81,-78,76,-87,71,-26,62,-81,57,67,-74,-23,-27,-32,-61,97,-49,-92,65,74,-19,2,21,5,75,-33,27,-7,-45,-81,98,-50,-60,51,-38,87,-74,-99,83,59,44,85,-64,-82,-47,-48,91,-20,-64,57,-46,17,-64,74,-78,87,-82,26,-20,-28,44,-44,22,83,-93,60,48,-91,61,31,68,5,16,80,-1,45,-68,-9,-75,-55,-75,-45,61,-40,-94,59,-53,-77,-15,3,-28,-71,58,93,89,42,53,37,27,-9,-55,-5,73,37,-47,-28,-41,-39,39,-17,5,40,14,-34,76,19,-97,99,41,-13,3,-87,-7,-62,82,-18,56,13,95,-16,-96,-83,55,53,53,-92,-97,88,-54,18,-52,50,-41,61,93,-65,-20,95,-65,-79,-41,14,-89,51,51,92,-90,8,-18,81,68,-14,97,23,-84,27,8,-82,15,53,36,62,3,94,0,-27,-94,79,-32,-60,77,4,53,87,-45,-18,56,-58,66,-61,-77,34,24,97,-66,16,24,41,34,-83,-6,-30,55,74,-59,-44,-53,-54,-88,-8,-14,88,95,-84,75,-73,-26,32,-32,-60,70,-32,50,-29,-35,84,86,65,25,20,58,96,66,-9,70,-93,23,93,-70,34,-15,-8,23,-20,7,-2,-16,58,-93,51,97,76,95,48,-53,-63,9,-89,-97,-66,7,37,-93,-26,-72,76,-43,50,47,-14,-15,-68,77,84,-11,-38,-18,72,-80,-11,0,-83,-58,-4,41,-34,32,-50,-24,11,-39,82,-51,-33,-67,-47,-79,-10,80,67,75,-58,75,30,-74,-36,91,-16,-87,-89,49,13,-96,91,-91,45,-43,17,71,9,-71,-91,-32,-46,-47,1,6,-50,67,-14,93,42,4,68,-28,29,-90,-60,-86,-78,-50,62,11,-46,30,19,75,86,-86,23,-28,-58,32,40,-28,84,-82,77,-89,84,-59,-96,26,44,48,75,-49,57,-85,-59,56,-58,-97,-33,-28,33,63,-53,-4,76,46,45,94,-22,-15,-34,-61,2,-80,-51,-14,-63,-71,88,81,77,40,-91,11,32,-51,-33,73,-72,34,-55,37,-26,-32,-89,-73,-86,55,-79,-31,-60,-37,7,18,-41,33,80,-4,61,68,-46,15,9,-38,-73,-82,10,-7,90,14,-96,-88,-48,-23,-44,-38,-20,-31,-83,0,14,-67,39,-78,50,98,31,30,-6,-31,-25,47,84,60,85,-89,77,-28,-20,44,85,-16,55,-63,37,-89,-25,-82,-43,-32,-6,47,0,-66,45,-73,-91,-24,33,-21,45,85,-74,6,45,87,16,0,-41,95,-56,-56,-44,76,-42,70,63,9,87,-80,77,-42,67,-46,-32,12,-19,-24,65,90,54,-13,75,56,92,21,43,-15,-79,78,-43,-59,99,13,-83,-43,-17,80,42,-53,76,19,-19,20,50,49,-90,-69,-98,74,97,33,-62,73,-34,-70,-29,86,14,-32,64,70,8,63,-40,2,96,19,-18,39,42,-42,-65,-76,55,84,72,64,91,50,15,89,-40,52,39,26,58,-90,12,-28,-23,-24,-81,61,-83,-44,-37,-87,74,44,28,17,79,63,40,11,24,-11,-25,16,-84,66,-18,-24,18,-79,-98,-24,-70,-10,24,-17,42,19,-79,58,74,-16,48,49,-95,-47,-57,60,-84,82,-29,17,-52,22,-67,-37,-12,-9,15,-94,11,16,-42,17,82,81,76,25,1,96,-17,-25,-20,-92,-99,-38,-39,-57,-78,-47,-98,-30,69,-51,91,78,-11,-20,-31,-96,-15,56,-3,20,-50,-21,1,-74,-96,78,-77,-36,-69,-21,-52,-92,17,8,-49,39,38,-71,85,-16,-22,76,-37,43,-44,8,23,18,-58,-80,-62,-9,-1,15,17,-21,-29,16,19,1,71,67,-15,-11,-48,12,-95,89,41,89,-26,95,65,13,38,98,-79,-39,16,-38,-42,53,53,33,-32,-53,-88,38,39,31,-84,10,-25,1,75,26,-87,56,16,30,45,66,25,-12,-21,-60,-14,-24,-22,-98,38,35,31,-32,-32,75,-9,-44,-9,-70,63,6,16,-62,83,-31,64,73,-75,-43,3,70,-77,-94,-65,1,-55,20,76,22,-2,-9,-43,-71,35,1,-96,-74,57,-6,-68,-3,77,25,35,60,93,-24,10,-82,32,90,64,31,95,98,-91,-83,-5,61,39,92,-47,72,-79,64,-26,-75,67,-92,-5,98,-19,-28,0,-84,-90,-7,-9,-4,-12,99,-14,-48,30,-42,-72,38,-25,22,0,-86,15,29,62,35,-7,-87,36,-40,96,-68,-64,-22,-20,35,-7,-34,-94,61,62,-7,37,-52,44,-32,-17,71,82,57,-6,-41,47,-91,87,9,20,-42,22,-66,-6,-5,-58,29,72,21,-58,-57,87,-53,-96,26,39,40,73,-17,84,-44,-68,67,89,2,-97,36,-13,90,-77,-93,-52,21,-83,18,-84,-42,-52,88,56,-11,-69,20,35,-89,-54,-49,27,95,33,-11,-71,41,-67,-82,-57,-65,31,29,-75,53,13,-51,-26,6,67,-34,64,91,-69,-3,-43,-62,-83,68,-52,-61,-81,52,-66,28,-59,-38,-30,-27,-43,-11,7,87,95,9,40,8,34,90,90,-22,-67,54,-31,-36,-72,25,1,-79,-7,26,-41,11,-22,-30,-83,-5,31,-14,67,87,74,-49,51,46,36,-9,-46,-29,-42,-78,48,-9,75,94,54,80,-4,-45,-99,89,57,-63,-23,-65,6,-7,29,-86,55,-27,78,7,1,29,-47,-63,97,-16,-16,-45,5,-67,45,-43,-96,-24,-86,-1,8,-85,-35,-35,-72,42,0,33,-88,-94,23,44,-44,1,-72,56,-92,-43,92,-95,40,-23,-41,-78,-14,81,-44,-34,-43,-31,64,41,-40,-70,-93,-13,48,-17,-80,36,-12,20,-20,43,-79,7,-24,-95,64,-31,-91,-19,22,-55,-20,84,-97,35,-50,-64,-96,90,77,-36,-80,83,50,44,-34,47,-19,30,-33,60,-49,-36,-55,26,-54,85,71,-46,-57,-30,-25,22,-46,-23,-66,-20,-10,-62,-52,-33,-22,-33,-73,-95,-88,-31,28,-31,75,71,-71,-74,-64,-50,29,-19,-88,0,11,-68,70,63,53,-99,-83,64,-42,6,78,5,49,-44,48,75,-63,36,-79,65,-95,96,36,-89,98,48,-63,27,-94,-74,-95,-6,-43,51,-43,86,51,-27,50,85,56,28,-33,5,60,92,-42,97,28,-22,39,10,-26,-48,20,-27,-99,33,76,82,58,80,-24,-85,31,32,-98,-40,82,28,-78,38,-66,-11,-57,93,-19,0,67,85,78,-17,-5,-71,35,91,-22,12,2,-45,-6,-40,-88,47,-48,43,-21,-70,-97,-39,57,-99,98,90,-11,-81,61,46,18,28,9,-27,-88,80,2,23,49,56,-65,-49,-89,5,10,-77,-48,61,42,8,90,21,45,25,21,44,15,87,62,-47,33,-43,81,-81,30,69,99,-91,-31,48,64,-20,98,75,84,-15,74,-86,-76,-7,21,90,-86,-34,15,34,86,-92,-2,25,-40,-68,82,-82,-73,-11,63,-74,-3,-68,50,-39,11,25,-87,-27,-89,63,-37,-89,-44,83,-99,-54,-74,-7,80,89,0,-22,14,36,-14,-27,31,13,61,-29,15,-65,3,-34,-27,90,90,-38,-60,77,-97,2,87,-42,-38,65,4,-12,-42,-39,-23,34,15,67,-30,78,-82,77,-32,55,-51,59,90,28,-98,-60,-5,69,1,35,46,-20,-63,11,38,-1,-24,-81,63,33,-44,-83,-33,47,83,13,2,77,-32,69,33,16,6,0,-79,7,39,15,-24,-83,-50,99,-3,-13,10,-88,62,62,-93,25,-5,-61,41,38,62,1,-72,-35,-21,-5,-89,88,-89,16,-12,-92,-76,-96,23,-24,-80,72,-25,-7,-64,61,4,97,23,-13,-1,-82,25,-83,32,-12,18,60,29,73,-45,39,61,-57,-67,-74,-73,-67,-71,49,8,-52,22,83,18,34,21,-78,9,-55,-14,-92,-61,-89,-98,71,-25,-4,8,-96,-54,39,20,83,58,52,-91,85,84,-63,34,-31,-39,-67,-48,78,44,50,77,-47,94,-37,-63,-67,-50,-62,80,2,10,-12,5,55,-95,-98,38,62,30,46,47,14,59,-41,83,-79,-32,-88,75,-88,61,29,-36,55,91,-22,65,-81,-8,45,20,-97,-89,-98,57,-85,-96,-27,76,33,-81,1,-75,55,36,-92,52,-96,95,27,-84,34,-43,-44,-34,-75,33,-69,-57,-74,53,62,-95,40,64,38,54,44,-89,7,-23,-93,84,1,61,20,-15,13,24,-42,-83,39,91,-27,94,-43,-2,5,-35,17,7,-82,-20,11,57,-79,-74,-12,64,-63,71,-59,-57,56,19,80,-24,-96,-7,76,-39,9,-8,-71,59,-36,-14,-66,68,50,50,-25,44,-70,62,-22,-50,64,65,-86,-99,13,-68,-80,-31,50,76,22,30,-31,-2,68,55,90,96,-9,-69,-41,24,98,85,-49,-50,6,-42,88,83,-16,52,25,-25,30,-61,6,49,-16,-67,26,-94,39,71,-19,7,3,-52,-19,93,-22,39,-6,-47,2,45,2,-92,-97,-10,91,-14,-81,-7,60,48,8,-57,-25,92,-25,77,97,-85,25,-45,-2,-71,2,78,98,56,-5,-30,-91,73,-85,10,80,93,76,48,-44,72,-58,-83,20,49,-64,94,18,11,48,16,2,-26,47,99,-21,-50,55,-23,-94,-73,46,-85]
    # print(len(my_list5))
    # print(max_sum(my_list5))
    print(max_sub_array(my_list5))


main()
