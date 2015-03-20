package jgibblda;

import org.junit.Test;

/**
 * Created by axelmagn on 3/12/15.
 */
public class EstimatorTest {
    public final static String[] estimatorArgs = {
            "-est",
            "-niters", "500",
            // "-nburnin", "200",
            "-nburnin", "0",
            "-ntopics", "11",
            "-dir", "src/test/resources",
            "-dfile", "random_1E3.gz"
    };

    @Test
    public void runEstimator() {
        LDA.main(estimatorArgs);
        // TODO: run cleanup
    }
}
