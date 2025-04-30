public class PlaneSeat {
    private int seatId;
    private boolean assigned;
    private int customerId;  // 0 means no customer assigned

    public PlaneSeat(int seatId) {
        this.seatId = seatId;
        this.assigned = false;
        this.customerId = 0;
    }

    public int getSeatID() {
        return seatId;
    }

    public int getCustomerID() {
        return customerId;
    }

    public boolean isOccupied() {
        return assigned;
    }

    public void assign(int custId) {
        if (!assigned) {
            this.customerId = custId;
            this.assigned = true;
        }
    }

    public void unAssign() {
        this.customerId = 0;
        this.assigned = false;
    }

    public String toString() {
        if (assigned) {
            return "SeatID " + seatId + " assigned to CustomerID " + customerId + ".";
        } else {
            return "SeatID " + seatId + " is empty.";
        }
    }
}
