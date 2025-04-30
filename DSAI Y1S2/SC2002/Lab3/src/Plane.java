import java.util.Arrays;
import java.util.Comparator;

public class Plane {
    private PlaneSeat[] seats;
    private int numEmptySeat;

    // Constructor: create 12 seats (seat IDs 1 to 12) and update the empty seat count
    public Plane() {
        seats = new PlaneSeat[12];
        for (int i = 0; i < 12; i++) {
            seats[i] = new PlaneSeat(i + 1);
        }
        numEmptySeat = 12;
    }

    // Create a copy of the seats array sorted by customerID (ascending) for assigned seats.
    // Seats with no customer (customerId==0) are considered larger so that assigned seats come first.
    private PlaneSeat[] sortSeatsByCustomerID() {
        PlaneSeat[] assignedSeats = Arrays.stream(seats)
                .filter(PlaneSeat::isOccupied)
                .toArray(PlaneSeat[]::new);

        Arrays.sort(assignedSeats, new Comparator<PlaneSeat>() {
            public int compare(PlaneSeat ps1, PlaneSeat ps2) {
                // compare customer IDs; if equal, compare by seat ID as tie-breaker
                int diff = ps1.getCustomerID() - ps2.getCustomerID();
                if (diff == 0) {
                    return ps1.getSeatID() - ps2.getSeatID();
                }
                return diff;
            }
        });
        return assignedSeats;
    }

    // Displays the number of empty seats.
    public void showNumEmptySeats() {
        System.out.println("There are " + numEmptySeat + " empty seats.");
    }

    // Displays a list of empty seats.
    public void showEmptySeats() {
        System.out.println("The following seats are empty:");
        for (PlaneSeat seat : seats) {
            if (!seat.isOccupied()) {
                System.out.println("SeatID " + seat.getSeatID());
            }
        }
    }

    // Displays assigned seats.
    // If bySeatId is true, the list is ordered by seat ID; otherwise, by customer ID.
    public void showAssignedSeats(boolean bySeatId) {
        PlaneSeat[] assignedSeats;
        if (bySeatId) {
            assignedSeats = Arrays.stream(seats)
                    .filter(PlaneSeat::isOccupied)
                    .sorted(Comparator.comparingInt(PlaneSeat::getSeatID))
                    .toArray(PlaneSeat[]::new);
        } else {
            assignedSeats = sortSeatsByCustomerID();
        }

        System.out.println("The seat assignments are as follow:");
        for (PlaneSeat seat : assignedSeats) {
            System.out.println("SeatID " + seat.getSeatID() + " assigned to CustomerID " + seat.getCustomerID() + ".");
        }
    }

    // Assign a customer to a seat.
    public void assignSeat(int seatId, int custId) {
        if (seatId < 1 || seatId > seats.length) {
            System.out.println("Invalid SeatID!");
            return;
        }

        PlaneSeat seat = seats[seatId - 1];
        if (seat.isOccupied()) {
            System.out.println("Seat already assigned to a customer.");
        } else {
            // Check that the customerID is not already used
            for (PlaneSeat s : seats) {
                if (s.isOccupied() && s.getCustomerID() == custId) {
                    System.out.println("CustomerID " + custId + " already has a seat.");
                    return;
                }
            }
            seat.assign(custId);
            numEmptySeat--;
            System.out.println("Seat Assigned!");
        }
    }

    // Unassign a seat.
    public void unAssignSeat(int seatId) {
        if (seatId < 1 || seatId > seats.length) {
            System.out.println("Invalid SeatID!");
            return;
        }
        PlaneSeat seat = seats[seatId - 1];
        if (seat.isOccupied()) {
            seat.unAssign();
            numEmptySeat++;
            System.out.println("Seat Unassigned!");
        } else {
            System.out.println("Seat is already empty.");
        }
    }
}
