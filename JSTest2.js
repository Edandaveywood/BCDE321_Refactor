// FEATURE 13 - Provide default values
const STORAGE_KEY = 'CycleLogEdan';

// FEATURE 1 - Create a whole, that acts as a Facade for parts
class CycleLog { // eslint-disable-line no-unused-vars
    constructor() {
        this.allMyRides = [];
        // Attributes used for editing a ride
        this.editedRide = null;
        this.editedRideIndex = null;


    // FEATURE 2 - Add a part
    addRide (newTitle, newDate, newDuration, newDistance) {
        newTitle = newTitle.trim();
        // FEATURE 10 - Validate inputs
        if (!newTitle) {
            return;
        }
        // FEATURE 13 - Provide default values
        let newId = this.allMyRides.length + 1;
        let newKPH = 1;
        let aNewRide = new Ride(newId, newTitle, newDate, newDuration, newDistance, newKPH);
        aNewRide.calculateKPH();

    // FEATURE 3 - Sort parts
    sortRides (input) {
        switch(input) {
            case "inputDistance":
                this.allMyRides.sort((a, b) => {
                    return a.distance < b.distance ? -1 : a.distance > b.distance ? 1 : 0;
                })
                break;
            case "inputDuration":
                this.allMyRides.sort((a, b) => {
                    return a.duration < b.duration ? -1 : a.duration > b.duration ? 1 : 0;
                })
                break;
            case "inputDate":
                this.allMyRides.sort((a, b)
            case "inputTitle":
                this.allMyRides.sort((a, b) => {
                    return a.title < b.title ? -1 : a.title > b.title ? 1 : 0;
                })
                break;
        }
    }

    // FEATURE 4 - Filter parts
    // FEATURE 12 - Calculation between many parts
    getShortRides() {
        let allShortRides = [];
		for (let aRide of this.allMyRides) {
			if (aRide.distance <= 5) {
				allShortRides.push( );
			}
		}
		return allShortRides;
    }

    // FEATURE 4 - Filter parts
    // FEATURE 12 - Calculation between many parts
    getLongRides() {
        let allLongRides = [];
		for (let aRide of this.allMyRides) {
			if (aRide.distance > 5) {
				allLongRides.push(aRide);
			}
		}
		return allLongRides;
    }

    // FEATURE 4 - Filter parts
    // FEATURE 12 - Calculation between many parts
    getRideBetweenDate(endDate) {
        let rideBetweenDates = [];
        let currentDate = new Date();
		for (let aRide of this.allMyRides) {
			if (aRide.startTime.getDate() < endDate.getDate() && aRide.startTime.getDate() != currentDate.getDate()) {
                rideBetweenDates.push(aRide);
			}
		}
		return rideBetweenDates;
    }

    // FEATURE 5 - Delete a selected part
    removeRide(targetRideTitle) {
        let index = this.allMyRides.findIndex(ride => ride.title == targetRideTitle);
        this.allMyRides.splice(index, 1);
    }

    // FEATURE 6 - Save all parts to LocalStorage
    save(allMyRides) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(allMyRides)); //CHANGE SETITEM
    }

    // FEATURE 7 - Load all parts from LocalStorage
    load() {
        return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'); //CHANGE GETITEM
    }

    // FEATURE 8 - Update / Edit a part
    startEdit(ride) {
        this.beforeEditTitleCache = ride.title;
        this.beforeEditDistanceCache = ride.distance;
        this.beforeEditDurationCache = ride.duration;
        this.editedRide = ride;
    }

    // FEATURE 8 - Update / Edit a part
    doneEdit(ride) {
        // FEATURE 10 - Validate inputs
        if (!ride) {
            return;
        }
        this.editedRide = null;
        ride.title = ride.title.trim();
        // FEATURE 10 - Validate inputs
        if (!ride.title) {
            this.removeRide(ride);
        }
    }

    // FEATURE 9 - Discard / revert edits to a part
    cancelEdit(ride) {
        this.editedRide = null;
        ride.title = this.beforeEditTitleCache;
        ride.distance = this.beforeEditDistanceCache;
        ride.duration = this.beforeEditDurationCache;
    }

    // FEATURE 12 - 12.	A calculation across many parts
    calculateTotalDistance() {
        let totalRideDistance = 0;
        for (let aRide of this.allMyRides) {
            if(!aRide.distance == 0) {
            totalRideDistance += aRide.distance;
        }
    }
    return totalRideDistance;
    }

    // FEATURE 12 - 12.	A calculation across many parts
    calculateAverageKPH() {
        let averageRideKPHarr = [];
        let averageRideKPH = 0;
		for (let aRide of this.allMyRides) {
            if(!aRide.kph == 0) {
                averageRideKPH += aRide.kph;
                averageRideKPHarr.push(aRide.speed);
            }
    }
    return averageRideKPH / (averageRideKPHarr.length);
    }

    // FEATURE 14 - Find a part given a search criterion
    findRideTitle(targetRideTitle) {
        return this.allMyRides.filter(function (ride) {
            return ride.title == targetRideTitle;
        });
    }

    // FEATURE 15 - Get all parts
    getAllRides() {
        return this.allMyRides;
    }
}

// FEATURE 2 - Add a part
class Ride { // eslint-disable-line no-unused-vars
    constructor (newId, newTitle, newDate,  newDuration, newDistance, newKPH) {
        // FEATURE 13 - Provide default values
        this.title = newTitle;
        this.id = newId;
        this.date = newDate;
        this.duration = newDuration;
        this.distance = newDistance;
        this.kph = newKPH;
        this.completed = false;
    }

    // // FEATURE 10 - Validate Input
     finishedRide(inputFinished) {
         if (inputFinished === true) {
             return this.completed = true;
         } else {
             return this.completed = false;
         }
     }

    // // FEATURE 11 - A caclulation within a part
     calculateDuration() {
         let time = this.endTime.getTime() - this.startTime.getTime();
         let minutes = time / 1000 / 60; // To get minute duration
         // let seconds = time - minutes * 60; // To get second duration
         // result += "Duration = " + minutes + " minutes " + seconds + " seconds";
         this.duration = minutes;
         return this.duration;
     }

    // FEATURE 11 - A caclulation within a part
    calculateKPH() {
        this.kph = (this.distance / this.duration) * 60;
        return this.kph;
    }

}

