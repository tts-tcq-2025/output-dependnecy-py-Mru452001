def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70, # High precipitation
        'humidity': 26,
        'windSpeedKMPH': 52  # High wind speed
    }

# NEW sensor stub to expose the bug
def highPrecipitationLowWindStub():
    return {
        'temperatureInC': 30, # Still high enough to enter outer 'if'
        'precipitation': 75, # High precipitation (>60)
        'humidity': 80,      # Can be anything, doesn't affect the bug
        'windSpeedKMPH': 40  # Low wind speed (<50)
    }

def report(sensorReader):
    read = sensorReader()
    weather = "Sunny Day" # Default weather - this is what the bug will cause it to remain

    if (read['temperatureInC'] > 25):
        if read['precipitation'] >= 20 and read['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif read['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
        

    return weather

def testRainy():
    weather = report(sensorStub)
    print(f"testRainy: {weather}")
    assert("rain" in weather)

def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)

    # Use the new stub here!
    weather = report(highPrecipitationLowWindStub) # <--- IMPORTANT CHANGE HERE
    print(f"testHighPrecipitation: {weather}")

    # This is the assertion that will FAIL and expose the bug
    assert(weather != "Sunny Day"), "Bug: High precipitation should not result in Sunny Day!"

if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
