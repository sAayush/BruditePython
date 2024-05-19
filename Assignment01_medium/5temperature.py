class Temp:
    def analyze(self, temp):
        print("Average temperature: ", sum(temp) / len(temp))
        print("Maximum temperature: ", max(temp))
        print("Minimum temperature: ", min(temp))


if __name__ == '__main__':
    t = Temp()
    temp = [23, 45, 67, 89, 12]
    t.analyze(temp)