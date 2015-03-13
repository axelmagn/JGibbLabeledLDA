package jgibblda;

import org.junit.Test;

/**
 * Created by axelmagn on 3/12/15.
 */
public class EstimatorTest {
    public final static String[] estimatorArgs = {
            "-est",
            "-niters", "2000",
            "-nburnin", "500",
            "-ntopics", "31662",
            "-dir", "src/test/resources",
            "-dfile", "sample_1E3.gz"
    };

    @Test
    public void runEstimator() {
        LDA.main(estimatorArgs);
        // TODO: run cleanup
    }
}
