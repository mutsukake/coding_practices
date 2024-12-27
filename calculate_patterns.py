# Calculate [①] Gender patterns
gender_patterns = 2  # "Male" or "Female"

# Calculate [②] Age patterns (including the possibility of no selections)
# There are 4 age groups, each can be selected or not
age_patterns = 2 ** 4  # 4 checkboxes, each can be on or off

# Calculate [③] Golf Experience patterns (including the possibility of no selections)
# There are 3 golf experience options
golf_experience_patterns = 2 ** 3  # 3 checkboxes

# Calculate [④] Registration Month patterns
# Each of Left and Right dropdowns can be unselected or select one of 4 months (Dec 2007 to Mar 2008)
# So 5 options for each (including "unselected")
registration_month_patterns = 5 * 5  # Left options * Right options

# Calculate [⑤] Total patterns (assuming independence)
total_patterns = gender_patterns * age_patterns * golf_experience_patterns * registration_month_patterns

# Now, adjust for invalid Registration Month patterns ([⑥])
# Invalid when Left date is later than Right date and both are selected
months = ['Unselected', 'Dec 2007', 'Jan 2008', 'Feb 2008', 'Mar 2008']
invalid_registration_patterns = 0
for left in range(1, 5):
    for right in range(1, 5):
        if left > right:
            invalid_registration_patterns += 1
# Total invalid patterns include combinations when both dates are selected and left > right

# [⑥] Number of invalid Registration Month patterns
print(f'[⑥] Invalid Registration Month patterns: {invalid_registration_patterns}')

# Adjusted Registration Month patterns
valid_registration_month_patterns = registration_month_patterns - invalid_registration_patterns

# Now, adjust for Age and Golf Experience patterns
# When only "10s" is selected in age, Golf Experience is hidden (only one pattern for Golf Experience)

from itertools import product

# Generate all age combinations
age_combinations = list(product([0, 1], repeat=4))

age_patterns_adjusted = 0
age_golf_patterns = 0

for age_comb in age_combinations:
    age_selected = sum(age_comb)
    if age_selected == 0:
        # No age selected, all ages considered
        age_patterns_adjusted += 1
        age_golf_patterns += golf_experience_patterns
    elif age_selected == 1 and age_comb[0] == 1:
        # Only "10s" selected
        age_patterns_adjusted += 1
        age_golf_patterns += 1  # Golf Experience is hidden
    else:
        # Other age selections
        age_patterns_adjusted += 1
        age_golf_patterns += golf_experience_patterns

# [②] Age patterns adjusted
print(f'[②] Age patterns: {age_patterns_adjusted}')

# [⑦] New Age and Golf Experience patterns
print(f'[⑦] New Age and Golf Experience patterns: {age_golf_patterns}')

# [①], [③], and [④] remain the same
print(f'[①] Gender patterns: {gender_patterns}')
print(f'[③] Golf Experience patterns: {golf_experience_patterns}')
print(f'[④] Registration Month patterns: {registration_month_patterns}')

# Calculate total valid patterns [⑧]
total_valid_patterns = gender_patterns * age_golf_patterns * valid_registration_month_patterns
print(f'[⑧] Total valid patterns: {total_valid_patterns}')