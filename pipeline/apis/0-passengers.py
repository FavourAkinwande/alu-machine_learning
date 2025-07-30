#!/usr/bin/env python3
"""
Module for creating a pandas DataFrame from a NumPy array.
"""

import pandas as pd
import numpy as np # Import numpy as it's implied by 'array' parameter


def from_numpy(array: np.ndarray) -> pd.DataFrame:
        """
            Creates a pandas DataFrame from a given NumPy array.

                Args:
                            array (np.ndarray): The NumPy array from which to create the DataFrame.
                                                        It is expected to have 8 columns to match the
                                                                                    defined column names.

                                                                                        Returns:
                                                                                                    pd.DataFrame: The newly created pandas DataFrame.
                                                                                                        """
                                                                                                            # Define the column names for the DataFrame.
                                                                                                                # Note: The original list had 'H' then 'G'. Assuming this is intentional.
                                                                                                                    columns_nw = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']

                                                                                                                        # Ensure the input array has the correct number of columns
                                                                                                                            # This is a good practice to prevent errors if the array shape doesn't match
                                                                                                                                if array.shape[1] != len(columns_nw):
                                                                                                                                            raise ValueError(
                                                                                                                                                                f"Input array must have {len(columns_nw)} columns, "
                                                                                                                                                                            f"but it has {array.shape[1]} columns."
                                                                                                                                                                                    )

                                                                                                                                                # Create the DataFrame using the NumPy array and specified column names.
                                                                                                                                                    df = pd.DataFrame(array, columns=columns_nw)

                                                                                                                                                        # Return the created DataFrame.
                                                                                                                                                            return df

                                                                                                                                                        # Example usage (for testing purposes, you can remove this in your final script)
                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                # Create a sample NumPy array (e.g., 5 rows, 8 columns)
                                                                                                                                                                    sample_array = np.random.rand(5, 8)
                                                                                                                                                                        
                                                                                                                                                                            # Create the DataFrame
                                                                                                                                                                                my_dataframe = from_numpy(sample_array)
                                                                                                                                                                                    
                                                                                                                                                                                        print("Successfully created DataFrame:")
                                                                                                                                                                                            print(my_dataframe)

                                                                                                                                                                                                # Example of incorrect array shape (will raise an error)
                                                                                                                                                                                                    try:
                                                                                                                                                                                                                bad_array = np.random.rand(3, 5) # 5 columns instead of 8
                                                                                                                                                                                                                        from_numpy(bad_array)
                                                                                                                                                                                                                            except ValueError as e:
                                                                                                                                                                                                                                        print(f"\nCaught expected error: {e}")

