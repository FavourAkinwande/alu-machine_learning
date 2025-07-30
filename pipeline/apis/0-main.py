#!/usr/bin/env python3
"""
Main script to test the availableShips function from the 0-passengers module.

This script demonstrates how to use the availableShips function by
fetching starships capable of carrying a specific number of passengers
and printing their names.
"""

# Dynamically import the availableShips function from the 0-passengers module.
# This is a common way to import modules when their names start with numbers
# or when the module name is determined dynamically.
availableShips = __import__('0-passengers').availableShips


def main():
        """
            Executes the main logic of the script.
                Calls availableShips with various passenger counts and prints the results.
                    This function directly addresses the test cases from the grading system.
                        """
                            # Define the passenger counts to test, matching the grading system's checks
                                passenger_counts_to_test = [4, 200000, 20000000, 310]

                                    for count in passenger_counts_to_test:
                                                print(f"\n--- Testing with passenger count = {count} ---")
                                                        
                                                                # Call the availableShips function
                                                                        ships = availableShips(count)

                                                                                # Print the names of the ships found
                                                                                        if ships:
                                                                                                    print(f"Available ships for {count} passengers:")
                                                                                                                for ship_name in ships:
                                                                                                                                    print(ship_name)
                                                                                                                                            else:
                                                                                                                                                            print(f"No ships found for {count} passengers.")

                                                                                                                                                                # You can also add other test cases if needed, for example:
                                                                                                                                                                    # print("\n--- Testing with passenger count = 0 (should show all ships with known capacity) ---")
                                                                                                                                                                        # ships_for_0 = availableShips(0)
                                                                                                                                                                            # if ships_for_0:
                                                                                                                                                                                #     print(f"Available ships for 0 passengers:")
                                                                                                                                                                                    #     for ship_name in ships_for_0:
                                                                                                                                                                                        #         print(ship_name)
                                                                                                                                                                                            # else:
                                                                                                                                                                                                #     print("No ships found for 0 passengers.")


                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                    main()

