import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();
queue.testMode = true;

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue.testMode = true;
    queue.clear();  // Clear the queue before each test
  });

  afterEach(() => {
    queue.testMode = false;  // Exit test mode after tests
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).toThrow('Jobs is not an array');
  });

  it('should create jobs in the queue if jobs is an array', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobIds = queue.testMode.jobs.map(job => job.id);
    expect(jobIds.length).toBe(2);
  });

  it('should create jobs with correct data in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];
    expect(job.data.phoneNumber).toBe('4153518780');
    expect(job.data.message).toBe('This is the code 1234 to verify your account');
  });
});
