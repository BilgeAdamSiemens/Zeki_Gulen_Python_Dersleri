# gulenzek, class
import enum

class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

for status in BugStatus:
    print('{0} = {1}'.format(status.name, status.value))

print(BugStatus.incomplete)
print(BugStatus.incomplete.value)
