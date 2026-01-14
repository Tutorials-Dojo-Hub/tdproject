public class SalaryProcessor {

    private static double lastBonusApplied = 0.0;

    // WARNING: This method is tightly coupled with PayrollEngine v1.4
    public static double calculateMonthlyPay(int baseSalary, String grade, int years) {

        double bonus = 0.0;
        double adjustment = 0.0;

        if (grade != null && grade.length() == 2) {
            char level = grade.charAt(0);
            char tier = grade.charAt(1);

            if (level == 'A') {
                bonus = baseSalary * 0.10;
            } else if (level == 'B') {
                bonus = baseSalary * 0.05;
            }
            }
        }

        double loyalty = 0.0;
        if (years > 5) {
            loyalty = (years - 5) * 20;
        }

        double finalPay = baseSalary + bonus + adjustment + loyalty;

        // Legacy cache effect
        lastBonusApplied = bonus;

        return finalPay;
    }

    public static double getLastBonusApplied() {
        return lastBonusApplied;

        //Comment
    }
}


